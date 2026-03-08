# ============================================================
# USER DATA MODULE
# File: modules/user_data_module.py
#
# Responsibility:
#   - Save and retrieve search history per user
#   - Save and retrieve favourites per user
#   - Save and retrieve dietary preferences per user
# ============================================================

import sqlite3
import json
from datetime import datetime

import os
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "recipeai.db")


# ------------------------------------------------------------------
# SEARCH HISTORY
# ------------------------------------------------------------------

def save_search(user_id: int, parsed_input: dict, results_count: int) -> None:
    """Save a search session to the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO search_history
            (user_id, dish_name, ingredients, dietary, allergies, results_count, searched_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        user_id,
        parsed_input.get("dish_name", ""),
        json.dumps(parsed_input.get("ingredients", [])),
        parsed_input.get("dietary", "both"),
        json.dumps(parsed_input.get("allergies", [])),
        results_count,
        datetime.utcnow().isoformat()
    ))

    conn.commit()
    conn.close()


def get_search_history(user_id: int, limit: int = 20) -> list:
    """
    Retrieve recent search history for a user.

    Returns:
        list[dict]: Most recent searches first.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM search_history
        WHERE user_id = ?
        ORDER BY searched_at DESC
        LIMIT ?
    """, (user_id, limit))

    rows = cursor.fetchall()
    conn.close()

    history = []
    for row in rows:
        history.append({
            "id"           : row["id"],
            "dish_name"    : row["dish_name"] or "Open Search",
            "ingredients"  : json.loads(row["ingredients"]) if row["ingredients"] else [],
            "dietary"      : row["dietary"],
            "allergies"    : json.loads(row["allergies"]) if row["allergies"] else [],
            "results_count": row["results_count"],
            "searched_at"  : row["searched_at"]
        })

    return history


def clear_search_history(user_id: int) -> None:
    """Delete all search history for a user."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM search_history WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()


# ------------------------------------------------------------------
# FAVOURITES
# ------------------------------------------------------------------

def save_favourite(user_id: int, recipe_id: str, recipe_name: str) -> dict:
    """
    Add a recipe to the user's favourites.

    Returns:
        dict: { "success": bool, "message": str }
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO favourites (user_id, recipe_id, recipe_name, saved_at)
            VALUES (?, ?, ?, ?)
        """, (user_id, recipe_id, recipe_name, datetime.utcnow().isoformat()))

        conn.commit()
        conn.close()
        return {"success": True, "message": "Added to favourites!"}

    except sqlite3.IntegrityError:
        return {"success": False, "message": "Already in your favourites."}


def remove_favourite(user_id: int, recipe_id: str) -> dict:
    """Remove a recipe from the user's favourites."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM favourites WHERE user_id = ? AND recipe_id = ?",
        (user_id, recipe_id)
    )
    conn.commit()
    conn.close()

    return {"success": True, "message": "Removed from favourites."}


def get_favourites(user_id: int) -> list:
    """
    Retrieve all favourites for a user.

    Returns:
        list[dict]: List of saved recipes.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM favourites
        WHERE user_id = ?
        ORDER BY saved_at DESC
    """, (user_id,))

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id"         : row["id"],
            "recipe_id"  : row["recipe_id"],
            "recipe_name": row["recipe_name"],
            "saved_at"   : row["saved_at"]
        }
        for row in rows
    ]


def is_favourite(user_id: int, recipe_id: str) -> bool:
    """Check if a recipe is already in a user's favourites."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT 1 FROM favourites WHERE user_id = ? AND recipe_id = ?",
        (user_id, recipe_id)
    )
    result = cursor.fetchone()
    conn.close()

    return result is not None


# ------------------------------------------------------------------
# USER PREFERENCES
# ------------------------------------------------------------------

def save_preferences(user_id: int, dietary: str, allergies: list) -> None:
    """Save or update dietary preferences for a user."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO user_preferences (user_id, dietary, allergies, updated_at)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(user_id) DO UPDATE SET
            dietary    = excluded.dietary,
            allergies  = excluded.allergies,
            updated_at = excluded.updated_at
    """, (
        user_id,
        dietary,
        json.dumps(allergies),
        datetime.utcnow().isoformat()
    ))

    conn.commit()
    conn.close()


def get_preferences(user_id: int) -> dict:
    """
    Get dietary preferences for a user.

    Returns:
        dict: { "dietary": str, "allergies": list }
              Defaults to "both" and [] if not set.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        "SELECT dietary, allergies FROM user_preferences WHERE user_id = ?",
        (user_id,)
    )
    row = cursor.fetchone()
    conn.close()

    if not row:
        return {"dietary": "both", "allergies": []}

    return {
        "dietary"  : row["dietary"],
        "allergies": json.loads(row["allergies"]) if row["allergies"] else []
    }

# ============================================================
# FAVOURITES MODULE
# File: modules/favorites_module.py
#
# Responsibility:
#   - Save a recipe to the favourites table in SQLite
#   - Fetch all saved favourites for display
#   - Delete a favourite by its ID
#
# Used by:
#   - App2.py routes: /favourites (GET, POST), /favourites/<id> (DELETE)
#
# Database table used:
#   favourites (id, recipe_name, recipe_emoji, saved_at)
# ============================================================

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "recipes.db")


def _get_connection():
    """Opens and returns a database connection with row_factory."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# ── CREATE ────────────────────────────────────────────────────────

def save_favourite(recipe_name: str, recipe_emoji: str = "🍽️") -> dict:
    """
    Saves a recipe to the favourites table.

    Args:
        recipe_name  (str): Name of the recipe to save.
        recipe_emoji (str): Emoji for the recipe (optional, defaults to 🍽️).

    Returns:
        dict: The newly saved favourite with its ID and timestamp,
              or an error message if it's already saved.
    """
    conn = _get_connection()

    # Check if already saved — avoid duplicates
    existing = conn.execute(
        "SELECT id FROM favourites WHERE LOWER(recipe_name) = LOWER(?)",
        (recipe_name,)
    ).fetchone()

    if existing:
        conn.close()
        return {"success": False, "error": f"'{recipe_name}' is already in your favourites."}

    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO favourites (recipe_name, recipe_emoji) VALUES (?, ?)",
        (recipe_name, recipe_emoji)
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return {
        "success" : True,
        "message" : f"'{recipe_name}' added to favourites!",
        "id"      : new_id
    }


# ── READ ──────────────────────────────────────────────────────────

def get_all_favourites() -> list:
    """
    Returns all saved favourites, newest first.

    Returns:
        list[dict]: Each dict has id, recipe_name, recipe_emoji, saved_at.
    """
    conn = _get_connection()
    rows = conn.execute(
        "SELECT * FROM favourites ORDER BY saved_at DESC"
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_favourite_count() -> int:
    """Returns the total number of saved favourites."""
    conn = _get_connection()
    count = conn.execute("SELECT COUNT(*) FROM favourites").fetchone()[0]
    conn.close()
    return count


# ── DELETE ────────────────────────────────────────────────────────

def delete_favourite(favourite_id: int) -> dict:
    """
    Removes a favourite by its ID.

    Args:
        favourite_id (int): The ID of the favourite to remove.

    Returns:
        dict: Success message or error if ID not found.
    """
    conn = _get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM favourites WHERE id = ?", (favourite_id,))
    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()

    if deleted:
        return {"success": True,  "message": f"Favourite #{favourite_id} removed."}
    else:
        return {"success": False, "error": f"No favourite found with ID {favourite_id}."}


def clear_all_favourites() -> int:
    """
    Deletes ALL favourites. Returns the number of rows deleted.
    """
    conn = _get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM favourites")
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    return deleted

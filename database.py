"""
database.py
-----------
SQLite setup for the AI Smart Recipe Generator.
Automatically creates ALL tables when App2.py starts.

Tables:
  - user_searches  : stores every search the user makes
  - favourites     : stores recipes the user has saved as favourites
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "recipes.db")


def get_connection():
    """Opens and returns a database connection with row_factory."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Creates all tables if they don't already exist.
    Called once at the bottom of App2.py — safe to run every time.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # ── Table 1: user_searches ────────────────────────────────
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_searches (
            id                  INTEGER  PRIMARY KEY AUTOINCREMENT,
            dish_name           TEXT,
            ingredients         TEXT,
            dietary_preference  TEXT,
            allergy_info        TEXT,
            results_found       INTEGER,
            searched_at         DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # ── Table 2: favourites ───────────────────────────────────
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS favourites (
            id           INTEGER  PRIMARY KEY AUTOINCREMENT,
            recipe_name  TEXT     NOT NULL,
            recipe_emoji TEXT     DEFAULT '🍽️',
            saved_at     DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()
    print("✅ Database ready — all tables loaded.")


def save_search(dish_name: str, ingredients: str,
                dietary_preference: str, allergy_info: str,
                results_found: int) -> int:
    """Saves one user search. Called from the /search route in App2.py."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO user_searches
            (dish_name, ingredients, dietary_preference, allergy_info, results_found)
        VALUES (?, ?, ?, ?, ?)
    """, (dish_name, ingredients, dietary_preference, allergy_info, results_found))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id


def get_all_searches() -> list:
    """Returns every saved search as a list of dicts, newest first."""
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM user_searches ORDER BY searched_at DESC"
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]

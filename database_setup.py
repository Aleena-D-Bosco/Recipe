# ============================================================
# DATABASE SETUP
# File: database_setup.py
#
# Responsibility:
#   - Create all SQLite tables on first run
#   - Safe to run multiple times (uses IF NOT EXISTS)
#
# Run once before starting the app:
#   python database_setup.py
# ============================================================

import sqlite3
from datetime import datetime

import os
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "recipeai.db")


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # ── Users ────────────────────────────────────────────────────
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            username      TEXT    NOT NULL UNIQUE,
            email         TEXT    NOT NULL UNIQUE,
            password_hash TEXT    NOT NULL,
            created_at    TEXT    NOT NULL
        )
    """)

    # ── User Preferences ─────────────────────────────────────────
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_preferences (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id          INTEGER NOT NULL UNIQUE,
            dietary          TEXT    DEFAULT 'both',
            allergies        TEXT    DEFAULT '',
            updated_at       TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    """)

    # ── Search History ───────────────────────────────────────────
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS search_history (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id        INTEGER NOT NULL,
            dish_name      TEXT    DEFAULT '',
            ingredients    TEXT    DEFAULT '',
            dietary        TEXT    DEFAULT 'both',
            allergies      TEXT    DEFAULT '',
            results_count  INTEGER DEFAULT 0,
            searched_at    TEXT    NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    """)

    # ── Favourites ───────────────────────────────────────────────
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS favourites (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER NOT NULL,
            recipe_id   TEXT    NOT NULL,
            recipe_name TEXT    NOT NULL,
            saved_at    TEXT    NOT NULL,
            UNIQUE(user_id, recipe_id),
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    """)

    conn.commit()
    conn.close()
    print("✅ Database initialised successfully at:", DB_PATH)


if __name__ == "__main__":
    init_db()

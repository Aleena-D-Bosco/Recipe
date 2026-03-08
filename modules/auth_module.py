# ============================================================
# AUTH MODULE
# File: modules/auth_module.py
#
# Responsibility:
#   - Register new users (hash password, store in DB)
#   - Login existing users (verify password)
#   - Fetch user by ID or email
#   - All auth logic stays here; Flask routes stay thin
# ============================================================

import sqlite3
import bcrypt
from datetime import datetime


DB_PATH = "recipeai.db"


# ------------------------------------------------------------------
# REGISTER
# ------------------------------------------------------------------

def register_user(username: str, email: str, password: str) -> dict:
    """
    Create a new user account.

    Returns:
        dict: { "success": bool, "message": str, "user_id": int|None }
    """
    if not username or not email or not password:
        return {"success": False, "message": "All fields are required.", "user_id": None}

    if len(password) < 6:
        return {"success": False, "message": "Password must be at least 6 characters.", "user_id": None}

    password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (username, email, password_hash, created_at) VALUES (?, ?, ?, ?)",
            (username.strip(), email.strip().lower(), password_hash, datetime.utcnow().isoformat())
        )
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()

        return {"success": True, "message": "Account created successfully!", "user_id": user_id}

    except sqlite3.IntegrityError as e:
        if "email" in str(e):
            return {"success": False, "message": "An account with this email already exists.", "user_id": None}
        if "username" in str(e):
            return {"success": False, "message": "This username is already taken.", "user_id": None}
        return {"success": False, "message": "Registration failed. Please try again.", "user_id": None}


# ------------------------------------------------------------------
# LOGIN
# ------------------------------------------------------------------

def login_user(email: str, password: str) -> dict:
    """
    Verify user credentials.

    Returns:
        dict: { "success": bool, "message": str, "user": dict|None }
    """
    if not email or not password:
        return {"success": False, "message": "Email and password are required.", "user": None}

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ?", (email.strip().lower(),))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return {"success": False, "message": "No account found with that email.", "user": None}

    if not bcrypt.checkpw(password.encode("utf-8"), row["password_hash"].encode("utf-8")):
        return {"success": False, "message": "Incorrect password.", "user": None}

    user = {
        "id"        : row["id"],
        "username"  : row["username"],
        "email"     : row["email"],
        "created_at": row["created_at"]
    }

    return {"success": True, "message": "Welcome back!", "user": user}


# ------------------------------------------------------------------
# FETCH USER
# ------------------------------------------------------------------

def get_user_by_id(user_id: int) -> dict | None:
    """Fetch a user record by their ID. Returns None if not found."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT id, username, email, created_at FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return None

    return {
        "id"        : row["id"],
        "username"  : row["username"],
        "email"     : row["email"],
        "created_at": row["created_at"]
    }

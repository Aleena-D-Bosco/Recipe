# ============================================================
# AUTH ROUTES
# File: auth_routes.py
#
# Add these routes to your main Flask app (app.py / App2.py).
# Make sure to:
#   1. pip install flask-login bcrypt
#   2. Run database_setup.py once before starting the app
#   3. Import and register this blueprint in your main app
#
# In your main app file, add:
#   from auth_routes import auth_bp
#   app.register_blueprint(auth_bp)
#   app.secret_key = "your-secret-key-here"   # change this!
#
# To protect any route, add:  @login_required
# To get the logged-in user:  current_user  (from flask_login)
# ============================================================

from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

from modules.auth_module import register_user, login_user as auth_login, get_user_by_id
from modules.user_data_module import (
    save_search, get_search_history, clear_search_history,
    save_favourite, remove_favourite, get_favourites, is_favourite,
    save_preferences, get_preferences
)

auth_bp = Blueprint("auth", __name__)


# ------------------------------------------------------------------
# Flask-Login User class
# ------------------------------------------------------------------

class User(UserMixin):
    def __init__(self, user_dict):
        self.id       = user_dict["id"]
        self.username = user_dict["username"]
        self.email    = user_dict["email"]


def init_login_manager(app):
    """Call this in your main app file after creating the Flask app."""
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login_page"   # redirect here if not logged in
    login_manager.login_message = "Please log in to access this page."

    @login_manager.user_loader
    def load_user(user_id):
        user_dict = get_user_by_id(int(user_id))
        return User(user_dict) if user_dict else None

    return login_manager


# ------------------------------------------------------------------
# ROUTES
# ------------------------------------------------------------------

@auth_bp.route("/login", methods=["GET"])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for("index"))       # already logged in → home
    return render_template("login.html")


@auth_bp.route("/login", methods=["POST"])
def login_post():
    email    = request.form.get("email", "")
    password = request.form.get("password", "")

    result = auth_login(email, password)

    if result["success"]:
        user = User(result["user"])
        login_user(user, remember=True)
        return redirect(url_for("index"))
    else:
        flash(result["message"], "error")
        return redirect(url_for("auth.login_page"))


@auth_bp.route("/register", methods=["POST"])
def register_post():
    username  = request.form.get("username", "")
    email     = request.form.get("email", "")
    password  = request.form.get("password", "")
    dietary   = request.form.get("dietary", "both")
    allergies_raw = request.form.get("allergies", "")

    result = register_user(username, email, password)

    if result["success"]:
        # Save dietary preferences right away
        allergies = [a.strip().lower() for a in allergies_raw.split(",") if a.strip()]
        save_preferences(result["user_id"], dietary, allergies)

        flash("Account created! Please log in.", "success")
        return redirect(url_for("auth.login_page"))
    else:
        flash(result["message"], "error")
        return redirect(url_for("auth.login_page") + "?tab=register")


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You've been logged out.", "success")
   return redirect(url_for("home"))


# ------------------------------------------------------------------
# USER DATA ROUTES (called via JS fetch from the frontend)
# ------------------------------------------------------------------

@auth_bp.route("/api/history", methods=["GET"])
@login_required
def api_get_history():
    history = get_search_history(current_user.id)
    return jsonify(history)


@auth_bp.route("/api/history/clear", methods=["POST"])
@login_required
def api_clear_history():
    clear_search_history(current_user.id)
    return jsonify({"success": True})


@auth_bp.route("/api/favourites", methods=["GET"])
@login_required
def api_get_favourites():
    favs = get_favourites(current_user.id)
    return jsonify(favs)


@auth_bp.route("/api/favourites/add", methods=["POST"])
@login_required
def api_add_favourite():
    data        = request.get_json()
    recipe_id   = data.get("recipe_id", "")
    recipe_name = data.get("recipe_name", "")
    result = save_favourite(current_user.id, recipe_id, recipe_name)
    return jsonify(result)


@auth_bp.route("/api/favourites/remove", methods=["POST"])
@login_required
def api_remove_favourite():
    data      = request.get_json()
    recipe_id = data.get("recipe_id", "")
    result    = remove_favourite(current_user.id, recipe_id)
    return jsonify(result)


@auth_bp.route("/api/preferences", methods=["GET"])
@login_required
def api_get_preferences():
    prefs = get_preferences(current_user.id)
    return jsonify(prefs)


@auth_bp.route("/api/preferences/save", methods=["POST"])
@login_required
def api_save_preferences():
    data      = request.get_json()
    dietary   = data.get("dietary", "both")
    allergies = data.get("allergies", [])
    save_preferences(current_user.id, dietary, allergies)
    return jsonify({"success": True})

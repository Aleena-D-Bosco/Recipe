from flask import Flask, render_template, request, jsonify, session
from flask_login import login_required, current_user

# ── Import each module ───────────────────────────────────────────
from modules.user_input_module      import parse_user_input, summarize_input
from modules.recommendation_module  import filter_recipes
from modules.recipe_database_module import get_all_recipes, get_recipe_count
from modules.substitute_module      import find_substitutes_for_missing
from modules.output_module          import (format_recipes_list,
                                            build_history_entry,
                                            format_all_browse_recipes)

# ── Auth & User Data ─────────────────────────────────────────────
from auth_routes                    import auth_bp, init_login_manager
from modules.user_data_module       import (save_search        as save_user_search,
                                            save_favourite     as save_user_favourite,
                                            remove_favourite   as remove_user_favourite,
                                            get_favourites     as get_user_favourites,
                                            is_favourite,
                                            get_search_history,
                                            clear_search_history,
                                            save_preferences,
                                            get_preferences)

# ── Database ─────────────────────────────────────────────────────
from database        import init_db, save_search, get_all_searches
from database_setup  import init_db as init_auth_db

# ── Flask app setup ──────────────────────────────────────────────
app = Flask(__name__)
app.secret_key = "recipe_secret_key_2024"

# ── Register Auth Blueprint & Login Manager ──────────────────────
app.register_blueprint(auth_bp)
init_login_manager(app)


# ============================================================
# ROUTE 1: HOME PAGE
# ============================================================
@app.route("/")
@login_required
def home():
    return render_template("index.html")


# ============================================================
# ROUTE 2: RECIPE SEARCH
# ============================================================
@app.route("/search", methods=["POST"])
@login_required
def search():
    data = request.get_json()

    raw_dish        = data.get("dish_name", "")
    raw_ingredients = data.get("ingredients", "")
    raw_dietary     = data.get("dietary", "both")
    raw_allergies   = data.get("allergies", "")

    parsed = parse_user_input(
        dish_name       = raw_dish,
        ingredients_raw = raw_ingredients,
        dietary         = raw_dietary,
        allergies_raw   = raw_allergies
    )

    matched_recipes = filter_recipes(
        user_ingredients   = parsed["ingredients"],
        dietary_preference = parsed["dietary"],
        allergies          = parsed["allergies"],
        dish_name          = parsed["dish_name"]
    )

    formatted = format_recipes_list(matched_recipes)

    # Save to old DB (keeps existing behaviour)
    save_search(
        dish_name          = parsed["dish_name"],
        ingredients        = ", ".join(parsed["ingredients"]),
        dietary_preference = parsed["dietary"],
        allergy_info       = ", ".join(parsed["allergies"]),
        results_found      = len(formatted)
    )

    # Save to new user-scoped search history
    save_user_search(current_user.id, parsed, len(formatted))

    # Keep session history for backwards compatibility
    if "history" not in session:
        session["history"] = []
    entry = build_history_entry(parsed, results_count=len(formatted))
    session["history"] = [entry] + session["history"][:9]
    session.modified = True

    return jsonify({"recipes": formatted, "total": len(formatted)})


# ============================================================
# ROUTE 3: BROWSE ALL RECIPES
# ============================================================
@app.route("/all_recipes", methods=["GET"])
@login_required
def all_recipes():
    raw_all   = get_all_recipes()
    formatted = format_all_browse_recipes(raw_all)
    return jsonify({"recipes": formatted, "count": get_recipe_count()})


# ============================================================
# ROUTE 4: SESSION HISTORY
# ============================================================
@app.route("/history", methods=["GET"])
@login_required
def get_history():
    history = session.get("history", [])
    return jsonify({"history": history})


# ============================================================
# ROUTE 5: NOTES
# ============================================================
@app.route("/notes", methods=["GET", "POST"])
@login_required
def notes():
    if request.method == "POST":
        data = request.get_json()
        session["notes"] = data.get("notes", "")
        session.modified = True
        return jsonify({"status": "saved"})
    else:
        return jsonify({"notes": session.get("notes", "")})


# ============================================================
# ROUTE 6: DB HISTORY
# ============================================================
@app.route("/db_history", methods=["GET"])
@login_required
def db_history():
    searches = get_all_searches()
    return jsonify({"searches": searches, "total": len(searches)})


# ============================================================
# ROUTE 7: USER SEARCH HISTORY (per-user, from new DB)
# ============================================================
@app.route("/user_history", methods=["GET"])
@login_required
def user_history():
    history = get_search_history(current_user.id)
    return jsonify({"history": history, "total": len(history)})


@app.route("/user_history/clear", methods=["POST"])
@login_required
def clear_user_history():
    clear_search_history(current_user.id)
    return jsonify({"success": True})


# ============================================================
# ROUTE 8: FAVOURITES  (now user-scoped)
# ============================================================
@app.route("/favourites", methods=["POST"])
@login_required
def add_favourite():
    data        = request.get_json()
    recipe_id   = (data.get("recipe_id")   or "").strip()
    recipe_name = (data.get("recipe_name") or "").strip()

    if not recipe_id or not recipe_name:
        return jsonify({"success": False, "error": "recipe_id and recipe_name are required."}), 400

    result = save_user_favourite(current_user.id, recipe_id, recipe_name)
    status = 201 if result["success"] else 409
    return jsonify(result), status


@app.route("/favourites", methods=["GET"])
@login_required
def list_favourites():
    favourites = get_user_favourites(current_user.id)
    return jsonify({"favourites": favourites, "total": len(favourites)})


@app.route("/favourites/remove", methods=["POST"])
@login_required
def delete_favourite():
    data      = request.get_json()
    recipe_id = (data.get("recipe_id") or "").strip()

    if not recipe_id:
        return jsonify({"success": False, "error": "recipe_id is required."}), 400

    result = remove_user_favourite(current_user.id, recipe_id)
    return jsonify(result)


@app.route("/favourites/check", methods=["GET"])
@login_required
def check_favourite():
    recipe_id = request.args.get("recipe_id", "")
    result    = is_favourite(current_user.id, recipe_id)
    return jsonify({"is_favourite": result})


# ============================================================
# ROUTE 9: USER PREFERENCES
# ============================================================
@app.route("/preferences", methods=["GET"])
@login_required
def get_prefs():
    prefs = get_preferences(current_user.id)
    return jsonify(prefs)


@app.route("/preferences", methods=["POST"])
@login_required
def save_prefs():
    data      = request.get_json()
    dietary   = data.get("dietary", "both")
    allergies = data.get("allergies", [])
    save_preferences(current_user.id, dietary, allergies)
    return jsonify({"success": True})


# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    init_db()       # existing DB
    init_auth_db()  # new users/auth DB
    print("=" * 55)
    print("  AI Smart Recipe Generator — Starting up")
    print(f"  Recipes loaded : {get_recipe_count()}")
    print("  Visit          : http://127.0.0.1:5000")
    print("=" * 55)
    app.run(debug=True)
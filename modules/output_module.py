# ============================================================
# MODULE 5: OUTPUT MODULE
# File: modules/output_module.py
#
# Responsibility:
#   - Format recipe data for clean JSON delivery to the frontend
#   - Build session history entries from parsed user input
#   - Serialise all recipe fields into safe, JSON-compatible types
#
# Note:
#   Visual rendering (HTML/CSS cards, modal, score bars) is handled
#   in templates/index.html and static/style.css.
#   This module only formats the data that gets sent to those views.
# ============================================================


def format_recipe_for_output(recipe: dict) -> dict:
    """
    Sanitise and standardise a recipe dictionary before sending
    it to the frontend as JSON.

    Ensures:
        - All list fields are actually lists (never None)
        - Numeric fields (calories, score) are proper numbers
        - Substitutes dict is always present (may be empty)
        - Missing ingredients list is always present (may be empty)

    Args:
        recipe (dict): Raw recipe dict from the recommendation module.

    Returns:
        dict: Clean, JSON-safe recipe dictionary.
    """
    return {
        "id"                 : str(recipe.get("id", "")),
        "name"               : str(recipe.get("name", "Unknown Recipe")),
        "emoji"              : str(recipe.get("emoji", "🍽️")),
        "category"           : str(recipe.get("category", "veg")),
        "ingredients"        : list(recipe.get("ingredients", [])),
        "steps"              : list(recipe.get("steps", [])),
        "cooking_time"       : str(recipe.get("cooking_time", "N/A")),
        "calories"           : int(recipe.get("calories", 0)),
        "tags"               : list(recipe.get("tags", [])),
        "score"              : float(recipe.get("score", 0)),
        "missing_ingredients": list(recipe.get("missing_ingredients", [])),
        "substitutes"        : dict(recipe.get("substitutes", {}))
    }


def format_recipes_list(recipes: list) -> list:
    """
    Apply format_recipe_for_output() across an entire list of recipes.

    Args:
        recipes (list[dict]): Raw list from the recommendation module.

    Returns:
        list[dict]: Cleaned list ready for jsonify().
    """
    return [format_recipe_for_output(r) for r in recipes]


def build_history_entry(parsed_input: dict, results_count: int) -> dict:
    """
    Create a compact history record from a user's search session.
    Stored in Flask session and shown on the Recipe History page.

    Args:
        parsed_input  (dict): Cleaned input from user_input_module.
        results_count (int) : Number of recipes returned by the search.

    Returns:
        dict: History entry with display-friendly fields.
    """
    return {
        "dish_name"    : parsed_input.get("dish_name") or "Open Search",
        "ingredients"  : parsed_input.get("ingredients", []),
        "dietary"      : parsed_input.get("dietary", "both"),
        "allergies"    : parsed_input.get("allergies", []),
        "results_count": results_count
    }


def format_all_browse_recipes(raw_recipes: list) -> list:
    """
    Format all recipes for the Browse All page.
    Score is fixed at 100 (no user comparison done), and
    missing/substitutes are empty since we're just browsing.

    Args:
        raw_recipes (list[dict]): Output of get_all_recipes() from the DB module.

    Returns:
        list[dict]: JSON-ready list for the /all_recipes endpoint.
    """
    formatted = []

    for recipe in raw_recipes:
        formatted.append({
            "id"                 : str(recipe.get("id", "")),
            "name"               : str(recipe.get("name", "")),
            "emoji"              : str(recipe.get("emoji", "🍽️")),
            "category"           : str(recipe.get("category", "veg")),
            "ingredients"        : list(recipe.get("ingredients", [])),
            "steps"              : list(recipe.get("steps", [])),
            "cooking_time"       : str(recipe.get("cooking_time", "")),
            "calories"           : int(recipe.get("calories", 0)),
            "tags"               : list(recipe.get("tags", [])),
            "score"              : 100,    # Browse mode → always full score
            "missing_ingredients": [],     # N/A in browse mode
            "substitutes"        : {}      # N/A in browse mode
        })

    return formatted
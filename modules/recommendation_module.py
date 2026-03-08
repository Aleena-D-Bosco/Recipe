# ============================================================
# MODULE 2: RECIPE RECOMMENDATION MODULE
# File: modules/recommendation_module.py
#
# SEARCH MODES:
#   - Dish name only   → show all recipes matching name/tag
#   - Ingredients only → show recipes with at least 1 ingredient match
#   - Both provided    → filter by name AND rank by ingredient match
#   - Neither          → browse mode, show everything at score=100
# ============================================================

from .recipe_database_module import RECIPE_DATABASE
from .substitute_module import find_substitutes_for_missing


def normalize(text: str) -> str:
    return text.strip().lower()


def calculate_match_score(user_ingredients: list, recipe_ingredients: list) -> float:
    if not recipe_ingredients:
        return 0.0
    user_set   = set(normalize(i) for i in user_ingredients)
    recipe_set = set(normalize(i) for i in recipe_ingredients)
    matched    = len(user_set & recipe_set)
    return round((matched / len(recipe_set)) * 100, 1)


def get_missing_ingredients(user_ingredients: list, recipe_ingredients: list) -> list:
    user_set   = set(normalize(i) for i in user_ingredients)
    recipe_set = set(normalize(i) for i in recipe_ingredients)
    return list(recipe_set - user_set)


def has_allergen(recipe_ingredients: list, allergy_list: list) -> bool:
    recipe_normalized = [normalize(i) for i in recipe_ingredients]
    for allergen in allergy_list:
        for ingredient in recipe_normalized:
            if allergen in ingredient:
                return True
    return False


def matches_dish_name(recipe: dict, dish_keyword: str) -> bool:
    """Check recipe name AND all tags for a partial keyword match."""
    if dish_keyword in normalize(recipe["name"]):
        return True
    for tag in recipe.get("tags", []):
        if dish_keyword in normalize(tag):
            return True
    return False


def filter_recipes(user_ingredients: list, dietary_preference: str,
                   allergies: list, dish_name: str = "") -> list:
    """
    Core recommendation engine.

    Search logic:
      • Dish name only   → return every matching recipe; score by pantry overlap
                           (score can be 0 — still shown so user sees the dish)
      • Ingredients only → return recipes with score > 0 (at least 1 match)
      • Both provided    → name-filter first, then rank by ingredient score
      • Neither          → browse mode, everything returned at score = 100
    """
    results         = []
    has_dish        = dish_name.strip() != ""
    has_ingredients = len(user_ingredients) > 0
    browse_mode     = not has_dish and not has_ingredients
    allergy_clean   = [normalize(a) for a in allergies]
    dish_keyword    = normalize(dish_name) if has_dish else ""

    for recipe_id, recipe in RECIPE_DATABASE.items():

        # ── Dietary filter ────────────────────────────────────────
        if dietary_preference == "veg" and recipe["category"] == "non-veg":
            continue

        # ── Allergy filter ────────────────────────────────────────
        if has_allergen(recipe["ingredients"], allergy_clean):
            continue

        # ── Dish name filter (only when user typed a dish name) ───
        if has_dish and not matches_dish_name(recipe, dish_keyword):
            continue

        # ── Score calculation ─────────────────────────────────────
        if browse_mode:
            score = 100
        elif has_ingredients:
            score = calculate_match_score(user_ingredients, recipe["ingredients"])
        else:
            # dish-name-only: show dish regardless of pantry score
            score = 0

        # ── Threshold: ingredients-only mode needs at least 1 match ──
        if has_ingredients and not has_dish and score == 0:
            continue

        # ── Missing + substitutes ─────────────────────────────────
        missing     = get_missing_ingredients(user_ingredients, recipe["ingredients"])
        substitutes = find_substitutes_for_missing(missing)

        results.append({
            "id"                 : recipe_id,
            "name"               : recipe["name"],
            "emoji"              : recipe["emoji"],
            "category"           : recipe["category"],
            "ingredients"        : recipe["ingredients"],
            "steps"              : recipe["steps"],
            "cooking_time"       : recipe["cooking_time"],
            "calories"           : recipe["calories"],
            "tags"               : recipe.get("tags", []),
            "score"              : score,
            "missing_ingredients": missing,
            "substitutes"        : substitutes
        })

    # Sort: dish-name-only → alphabetical; otherwise → score descending
    if has_dish and not has_ingredients:
        results.sort(key=lambda r: r["name"])
    else:
        results.sort(key=lambda r: r["score"], reverse=True)

    return results
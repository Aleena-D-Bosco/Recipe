# ============================================================
# MODULE 1: USER INPUT MODULE
# File: modules/user_input_module.py
#
# Responsibility:
#   - Accept and validate all inputs from the user
#   - Parse raw comma-separated strings into clean lists
#   - Return a structured input dictionary for other modules
#
# Inputs accepted:
#   - dish_name        : optional string (name of desired dish)
#   - ingredients_raw  : comma-separated string of available ingredients
#   - dietary          : "veg", "non-veg", or "both"
#   - allergies_raw    : comma-separated string of allergy items
# ============================================================


def parse_user_input(dish_name: str, ingredients_raw: str,
                     dietary: str, allergies_raw: str) -> dict:
    """
    Parse and validate raw user inputs from the web form.

    Args:
        dish_name      (str): Optional name/keyword for the dish.
        ingredients_raw(str): Comma-separated ingredients the user has.
        dietary        (str): Dietary preference — "veg", "non-veg", or "both".
        allergies_raw  (str): Comma-separated allergens to avoid.

    Returns:
        dict: A clean, validated input dictionary with keys:
              dish_name, ingredients, dietary, allergies, errors
    """

    errors = []  # Collect any validation messages

    # --- Clean dish name ---
    dish_name_clean = dish_name.strip() if dish_name else ""

    # --- Parse ingredients list ---
    # Split on commas, strip whitespace, discard empty entries
    ingredients = [
        item.strip().lower()
        for item in ingredients_raw.split(",")
        if item.strip()
    ]

    # --- Validate dietary preference ---
    valid_dietary_options = ["veg", "non-veg", "both"]
    dietary_clean = dietary.strip().lower() if dietary else "both"
    if dietary_clean not in valid_dietary_options:
        dietary_clean = "both"  # Default fallback
        errors.append(f"Invalid dietary choice '{dietary}'. Defaulting to 'both'.")

    # --- Parse allergies list ---
    allergies = [
        item.strip().lower()
        for item in allergies_raw.split(",")
        if item.strip()
    ]

    # --- Build and return structured input ---
    parsed_input = {
        "dish_name"  : dish_name_clean,
        "ingredients": ingredients,
        "dietary"    : dietary_clean,
        "allergies"  : allergies,
        "errors"     : errors
    }

    return parsed_input


def summarize_input(parsed_input: dict) -> str:
    """
    Return a human-readable summary of what the user entered.
    Useful for logging and session history display.

    Args:
        parsed_input (dict): Output from parse_user_input().

    Returns:
        str: One-line summary string.
    """
    dish   = parsed_input["dish_name"] or "Any dish"
    ings   = ", ".join(parsed_input["ingredients"]) or "None specified"
    diet   = parsed_input["dietary"]
    allerg = ", ".join(parsed_input["allergies"]) or "None"

    return (
        f"Dish: {dish} | "
        f"Ingredients: {ings} | "
        f"Diet: {diet} | "
        f"Allergies: {allerg}"
    )
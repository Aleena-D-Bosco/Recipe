# ============================================================
# MODULE 4: SUBSTITUTE RECOMMENDATION MODULE
# File: modules/substitute_module.py
#
# Responsibility:
#   - Maintain a dictionary of ingredient substitutes
#   - Given a list of missing ingredients, return smart alternatives
#   - Keep substitute logic entirely rule-based (no APIs or ML)
#
# How it works:
#   Each key in SUBSTITUTES is a common ingredient name (lowercase).
#   The value is a list of 2–4 practical substitutes a home cook
#   might realistically have or easily find.
# ============================================================


# ------------------------------------------------------------------
# SUBSTITUTE DICTIONARY
# Keys   : common ingredient names (all lowercase)
# Values : list of substitute options (most accessible first)
# ------------------------------------------------------------------

SUBSTITUTES = {

    # ── Dairy & Fats ─────────────────────────────────────────────
    "butter"       : ["margarine", "coconut oil", "olive oil"],
    "milk"         : ["almond milk", "oat milk", "coconut milk"],
    "cream"        : ["coconut cream", "evaporated milk", "Greek yogurt"],
    "mozzarella"   : ["provolone", "fontina", "cheddar"],
    "parmesan"     : ["pecorino romano", "grana padano", "nutritional yeast"],
    "cheese"       : ["nutritional yeast", "tofu-based cheese", "cashew cheese"],
    "yogurt"       : ["sour cream", "buttermilk", "coconut yogurt"],

    # ── Proteins ─────────────────────────────────────────────────
    "eggs"         : ["flax egg (1 tbsp flaxseed + 3 tbsp water)",
                      "applesauce (¼ cup)", "yogurt (¼ cup)"],
    "bacon"        : ["turkey bacon", "smoked tempeh", "sun-dried tomatoes"],
    "chicken"      : ["tofu", "paneer", "chickpeas", "jackfruit"],
    "beef"         : ["turkey mince", "mushrooms", "lentils", "black beans"],

    # ── Oils & Condiments ────────────────────────────────────────
    "olive oil"    : ["vegetable oil", "avocado oil", "sunflower oil"],
    "sesame oil"   : ["toasted peanut oil", "walnut oil", "olive oil"],
    "soy sauce"    : ["tamari", "coconut aminos", "worcestershire sauce"],

    # ── Aromatics ────────────────────────────────────────────────
    "garlic"       : ["garlic powder (¼ tsp per clove)", "shallots", "asafoetida (pinch)"],
    "ginger"       : ["ground ginger (¼ tsp)", "galangal", "mace"],
    "onion"        : ["shallots", "leeks", "green onion"],

    # ── Acids & Citrus ───────────────────────────────────────────
    "lemon"        : ["lime", "white wine vinegar", "orange juice"],
    "lime"         : ["lemon", "white vinegar", "tamarind paste"],

    # ── Grains & Starches ────────────────────────────────────────
    "flour"        : ["almond flour", "oat flour", "rice flour"],
    "rice"         : ["quinoa", "cauliflower rice", "couscous"],
    "pasta"        : ["zucchini noodles", "rice noodles", "spaghetti squash"],
    "cornstarch"   : ["arrowroot powder", "potato starch", "tapioca starch"],
    "taco shells"  : ["flour tortillas", "lettuce wraps", "corn tortillas"],

    # ── Sweeteners & Leaveners ───────────────────────────────────
    "sugar"        : ["honey", "maple syrup", "coconut sugar"],
    "baking powder": ["baking soda + cream of tartar (1:2)", "self-raising flour"],
    "yeast"        : ["baking powder (for quick breads)", "sourdough starter"],
    "vanilla"      : ["vanilla bean paste", "almond extract (half quantity)", "maple extract"],

    # ── Vegetables ───────────────────────────────────────────────
    "tomato"       : ["sun-dried tomato", "roasted red pepper", "pumpkin puree"],
    "spinach"      : ["kale", "arugula", "Swiss chard"],
    "mushroom"     : ["zucchini", "eggplant", "sun-dried tomatoes"],
    "broccoli"     : ["cauliflower", "broccolini", "green beans"],
    "carrot"       : ["parsnip", "sweet potato", "butternut squash"],
    "lettuce"      : ["spinach", "arugula", "cabbage"],
    "bell pepper"  : ["poblano pepper", "zucchini", "celery"],
    "cucumber"     : ["zucchini", "celery", "jicama"],

    # ── Legumes ──────────────────────────────────────────────────
    "lentils"      : ["split peas", "chickpeas", "kidney beans"],

    # ── Fruits ───────────────────────────────────────────────────
    "banana"       : ["plantain", "applesauce", "mango puree"],

    # ── Spices & Herbs ───────────────────────────────────────────
    "cumin"        : ["caraway seeds", "chili powder", "paprika"],
    "turmeric"     : ["saffron", "annatto", "yellow mustard (small amount)"],
    "coriander"    : ["parsley", "cilantro stems", "cumin"],
    "thyme"        : ["oregano", "rosemary", "marjoram"],
    "basil"        : ["oregano", "fresh mint", "tarragon"],
    "garam masala" : ["curry powder", "allspice + cumin mix", "ras el hanout"],
    "chili"        : ["cayenne pepper (half amount)", "paprika", "hot sauce"],
    "black pepper" : ["white pepper", "cayenne (pinch)", "red pepper flakes"],

    # ── Miscellaneous ────────────────────────────────────────────
    "tomato sauce" : ["crushed tomatoes + seasoning", "salsa", "pesto"],
}


# ------------------------------------------------------------------
# MAIN FUNCTION — used by the recommendation module
# ------------------------------------------------------------------

def find_substitutes_for_missing(missing_ingredients: list) -> dict:
    """
    For each ingredient the user is missing, look up a substitute.

    Args:
        missing_ingredients (list): Ingredient names the user doesn't have.

    Returns:
        dict: {ingredient_name: [substitute1, substitute2, ...]}
              Only includes ingredients for which a substitute exists.

    Example:
        find_substitutes_for_missing(["butter", "eggs", "xyz"])
        →  {
               "butter": ["margarine", "coconut oil", "olive oil"],
               "eggs"  : ["flax egg ...", "applesauce ...", "yogurt ..."]
           }
        ("xyz" is excluded — no substitute found)
    """
    suggestions = {}

    for ingredient in missing_ingredients:
        key = ingredient.strip().lower()

        if key in SUBSTITUTES:
            suggestions[ingredient] = SUBSTITUTES[key]

    return suggestions


# ------------------------------------------------------------------
# UTILITY — list all ingredients we have substitutes for
# ------------------------------------------------------------------

def get_all_substitutable_ingredients() -> list:
    """
    Return a sorted list of every ingredient that has a known substitute.
    Useful for testing or displaying coverage info.

    Returns:
        list[str]: Sorted list of ingredient names.
    """
    return sorted(SUBSTITUTES.keys())
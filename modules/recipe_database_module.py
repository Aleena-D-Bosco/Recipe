# ============================================================
# MODULE 3: RECIPE DATABASE MODULE
# File: modules/recipe_database_module.py
#
# Total recipes: 49
#   Original  : 10
#   Indian    : 10  (+ existing chicken_curry, lentil_soup = 12 total Indian)
#   French    : 5
#   Chinese   : 3
#   Korean    : 3
#   Japanese  : 3
#   Spanish   : 3
#   Desserts  : 5
#   Drinks    : 5
#   Snacks    : 5
# ============================================================


RECIPE_DATABASE = {

    # ════════════════════════════════════════════════════════
    # ORIGINAL RECIPES (kept exactly as-is)
    # ════════════════════════════════════════════════════════

    "spaghetti_carbonara": {
        "name"        : "Spaghetti Carbonara",
        "emoji"       : "🍝",
        "category"    : "non-veg",
        "ingredients" : ["spaghetti", "eggs", "bacon", "parmesan",
                         "black pepper", "salt", "garlic"],
        "steps"       : [
            "Boil spaghetti in salted water until al dente (8–10 minutes).",
            "Fry bacon in a pan until crispy; add minced garlic and cook 1 minute.",
            "Whisk eggs with grated parmesan and black pepper in a bowl.",
            "Drain pasta, reserving ½ cup pasta water.",
            "Remove pan from heat, add pasta to bacon, then pour egg mixture while tossing quickly.",
            "Add pasta water gradually to create a creamy sauce. Serve immediately."
        ],
        "cooking_time": "20 minutes",
        "calories"    : 520,
        "tags"        : ["italian", "pasta", "quick"]
    },

    "mushroom_pasta": {
        "name"        : "Creamy Mushroom Pasta",
        "emoji"       : "🍄",
        "category"    : "veg",
        "ingredients" : ["pasta", "mushroom", "garlic", "cream", "butter",
                         "parmesan", "thyme", "salt", "pepper", "olive oil"],
        "steps"       : [
            "Cook pasta in salted boiling water until al dente.",
            "Melt butter in a pan; sauté garlic 1 minute.",
            "Add sliced mushrooms; cook until golden and moisture evaporates (6–8 min).",
            "Add thyme and pour in cream; simmer 3 minutes.",
            "Stir in parmesan until sauce thickens.",
            "Toss drained pasta in the sauce.",
            "Season generously and serve with extra parmesan."
        ],
        "cooking_time": "25 minutes",
        "calories"    : 460,
        "tags"        : ["italian", "pasta", "creamy"]
    },

    "vegetable_stir_fry": {
        "name"        : "Vegetable Stir Fry",
        "emoji"       : "🥦",
        "category"    : "veg",
        "ingredients" : ["broccoli", "carrot", "bell pepper", "onion", "garlic",
                         "soy sauce", "olive oil", "ginger", "cornstarch"],
        "steps"       : [
            "Chop all vegetables into bite-sized pieces.",
            "Heat olive oil in a wok or large pan over high heat.",
            "Add garlic and ginger, stir for 30 seconds.",
            "Add harder vegetables (carrot, broccoli) first; stir-fry 3 minutes.",
            "Add bell pepper and onion; stir-fry another 2 minutes.",
            "Mix soy sauce and cornstarch with 2 tbsp water; pour over veggies.",
            "Toss everything together and serve hot over rice."
        ],
        "cooking_time": "15 minutes",
        "calories"    : 180,
        "tags"        : ["asian", "healthy", "quick", "stir fry"]
    },

    "egg_fried_rice": {
        "name"        : "Egg Fried Rice",
        "emoji"       : "🍳",
        "category"    : "veg",
        "ingredients" : ["rice", "eggs", "onion", "garlic", "soy sauce",
                         "sesame oil", "green onion", "oil", "salt", "pepper"],
        "steps"       : [
            "Cook rice and let it cool completely (best if day-old).",
            "Beat eggs with a pinch of salt.",
            "Heat oil in a wok; scramble eggs lightly, then push to side.",
            "Add garlic and onion; sauté 2 minutes.",
            "Add cold rice; break up clumps and stir-fry 3 minutes.",
            "Drizzle soy sauce and sesame oil; toss well.",
            "Season with pepper; garnish with sliced green onion."
        ],
        "cooking_time": "20 minutes",
        "calories"    : 310,
        "tags"        : ["asian", "quick", "rice"]
    },

    "chicken_curry": {
        "name"        : "Chicken Curry",
        "emoji"       : "🍛",
        "category"    : "non-veg",
        "ingredients" : ["chicken", "onion", "tomato", "garlic", "ginger",
                         "cumin", "coriander", "turmeric", "chili",
                         "oil", "salt", "garam masala"],
        "steps"       : [
            "Cut chicken into pieces and marinate with turmeric and salt for 15 minutes.",
            "Heat oil; sauté sliced onions until golden brown.",
            "Add garlic-ginger paste; cook 2 minutes until fragrant.",
            "Add chopped tomatoes; cook until mushy and oil separates.",
            "Add cumin, coriander, chili powder; stir 1 minute.",
            "Add chicken pieces; brown on all sides for 5 minutes.",
            "Pour in 1 cup water, cover and simmer 20 minutes.",
            "Finish with garam masala and fresh coriander. Serve with rice or naan."
        ],
        "cooking_time": "45 minutes",
        "calories"    : 420,
        "tags"        : ["indian", "spicy", "curry", "non-veg"]
    },

    "lentil_soup": {
        "name"        : "Lentil Soup",
        "emoji"       : "🍲",
        "category"    : "veg",
        "ingredients" : ["lentils", "onion", "garlic", "carrot", "tomato",
                         "cumin", "turmeric", "olive oil", "salt", "lemon", "spinach"],
        "steps"       : [
            "Rinse lentils thoroughly under cold water.",
            "Heat olive oil; sauté diced onion, garlic and carrot until softened.",
            "Add cumin and turmeric; toast 30 seconds.",
            "Add lentils, chopped tomato and 4 cups water or broth.",
            "Bring to boil, then simmer covered for 25 minutes.",
            "Stir in spinach and cook 2 more minutes.",
            "Squeeze in lemon juice, season and serve warm."
        ],
        "cooking_time": "35 minutes",
        "calories"    : 220,
        "tags"        : ["soup", "healthy", "indian", "veg"]
    },

    "margherita_pizza": {
        "name"        : "Margherita Pizza",
        "emoji"       : "🍕",
        "category"    : "veg",
        "ingredients" : ["flour", "yeast", "tomato sauce", "mozzarella",
                         "basil", "olive oil", "salt", "sugar", "water"],
        "steps"       : [
            "Mix flour, yeast, sugar, salt, olive oil, and warm water; knead 8 minutes.",
            "Let dough rise covered for 1 hour until doubled.",
            "Preheat oven to 220°C (430°F).",
            "Roll dough into a round base on floured surface.",
            "Spread tomato sauce evenly, leaving a 1-inch border.",
            "Arrange sliced mozzarella on top.",
            "Bake 12–15 minutes until crust is golden.",
            "Top with fresh basil and a drizzle of olive oil before serving."
        ],
        "cooking_time": "1 hour 30 minutes",
        "calories"    : 285,
        "tags"        : ["italian", "baked", "pizza", "veg"]
    },

    "grilled_chicken_salad": {
        "name"        : "Grilled Chicken Salad",
        "emoji"       : "🥗",
        "category"    : "non-veg",
        "ingredients" : ["chicken", "lettuce", "tomato", "cucumber",
                         "olive oil", "lemon", "garlic", "salt", "pepper", "parmesan"],
        "steps"       : [
            "Season chicken with garlic, salt, pepper, and olive oil.",
            "Grill chicken 6–7 minutes per side until cooked through.",
            "Let chicken rest 5 minutes, then slice thinly.",
            "Tear lettuce, chop tomato and cucumber into chunks.",
            "Whisk olive oil, lemon juice, salt and pepper for dressing.",
            "Assemble salad, top with chicken slices.",
            "Drizzle dressing and sprinkle parmesan. Serve immediately."
        ],
        "cooking_time": "25 minutes",
        "calories"    : 290,
        "tags"        : ["salad", "healthy", "protein", "non-veg"]
    },

    "banana_pancakes": {
        "name"        : "Banana Pancakes",
        "emoji"       : "🥞",
        "category"    : "veg",
        "ingredients" : ["banana", "eggs", "flour", "milk", "butter",
                         "baking powder", "sugar", "salt", "vanilla"],
        "steps"       : [
            "Mash ripe banana in a bowl until smooth.",
            "Mix in eggs, milk, melted butter and vanilla extract.",
            "Sift in flour, baking powder, sugar and salt; mix until just combined.",
            "Heat a non-stick pan over medium heat; lightly butter it.",
            "Pour ¼ cup batter per pancake; cook until bubbles form (2–3 min).",
            "Flip and cook another 1–2 minutes until golden.",
            "Serve with honey, maple syrup or fresh fruit."
        ],
        "cooking_time": "20 minutes",
        "calories"    : 240,
        "tags"        : ["breakfast", "sweet", "quick", "pancakes", "veg"]
    },

    "beef_tacos": {
        "name"        : "Beef Tacos",
        "emoji"       : "🌮",
        "category"    : "non-veg",
        "ingredients" : ["beef", "taco shells", "onion", "garlic", "tomato",
                         "lettuce", "cheese", "cumin", "chili powder",
                         "oil", "salt", "lime"],
        "steps"       : [
            "Brown ground beef in a pan over medium-high heat; drain fat.",
            "Add diced onion and garlic; cook 3 minutes.",
            "Season with cumin, chili powder and salt; mix well.",
            "Warm taco shells in oven at 180°C for 3 minutes.",
            "Fill shells with beef mixture.",
            "Top with shredded lettuce, diced tomato, cheese.",
            "Squeeze fresh lime and serve immediately."
        ],
        "cooking_time": "20 minutes",
        "calories"    : 380,
        "tags"        : ["mexican", "quick", "tacos", "non-veg"]
    },


    # ════════════════════════════════════════════════════════
    # 🇮🇳 INDIAN CUISINES (10 new)
    # ════════════════════════════════════════════════════════

    "butter_chicken": {
        "name"        : "Butter Chicken",
        "emoji"       : "🍗",
        "category"    : "non-veg",
        "ingredients" : ["chicken", "butter", "cream", "tomato", "onion",
                         "garlic", "ginger", "garam masala", "turmeric",
                         "chili powder", "coriander powder", "salt", "oil"],
        "steps"       : [
            "Marinate chicken in yogurt, turmeric, and chili powder for 30 minutes.",
            "Grill or pan-fry chicken until charred; set aside.",
            "Melt butter; sauté onion, garlic and ginger until golden.",
            "Add tomatoes and all spices; cook until oil separates.",
            "Blend the sauce smooth; return to pan.",
            "Add grilled chicken and cream; simmer 10 minutes.",
            "Garnish with cream and coriander. Serve with naan or rice."
        ],
        "cooking_time": "50 minutes",
        "calories"    : 490,
        "tags"        : ["indian", "curry", "non-veg", "butter chicken"]
    },

    "palak_paneer": {
        "name"        : "Palak Paneer",
        "emoji"       : "🥬",
        "category"    : "veg",
        "ingredients" : ["paneer", "spinach", "onion", "tomato", "garlic",
                         "ginger", "cumin", "garam masala", "cream",
                         "turmeric", "chili", "oil", "salt"],
        "steps"       : [
            "Blanch spinach in boiling water 2 minutes; drain and blend smooth.",
            "Heat oil; sauté cumin seeds until they splutter.",
            "Add onion, garlic, ginger; cook until golden.",
            "Add tomato and spices; cook until oil separates.",
            "Pour in spinach purée; simmer 5 minutes.",
            "Add cubed paneer and cream; cook 3 more minutes.",
            "Season and serve hot with roti or rice."
        ],
        "cooking_time": "30 minutes",
        "calories"    : 320,
        "tags"        : ["indian", "veg", "paneer", "palak"]
    },

    "biryani": {
        "name"        : "Chicken Biryani",
        "emoji"       : "🍚",
        "category"    : "non-veg",
        "ingredients" : ["basmati rice", "chicken", "onion", "yogurt", "tomato",
                         "garlic", "ginger", "biryani masala", "turmeric",
                         "saffron", "milk", "ghee", "mint", "oil", "salt"],
        "steps"       : [
            "Marinate chicken in yogurt, garlic-ginger paste, biryani masala and salt for 1 hour.",
            "Parboil basmati rice (70% cooked); drain and set aside.",
            "Fry thinly sliced onions until golden and crispy; remove half for garnish.",
            "Cook marinated chicken in the same oil with tomatoes until done.",
            "Layer rice over chicken in pot; add saffron-infused milk and ghee.",
            "Seal pot with foil and lid; cook on low flame 25 minutes (dum).",
            "Gently mix, garnish with fried onions and fresh mint. Serve hot."
        ],
        "cooking_time": "1 hour 30 minutes",
        "calories"    : 550,
        "tags"        : ["indian", "rice", "non-veg", "biryani"]
    },

    "dal_tadka": {
        "name"        : "Dal Tadka",
        "emoji"       : "🫕",
        "category"    : "veg",
        "ingredients" : ["yellow lentils", "onion", "tomato", "garlic", "ginger",
                         "cumin seeds", "turmeric", "chili", "ghee",
                         "coriander", "salt", "lemon"],
        "steps"       : [
            "Pressure cook lentils with turmeric, salt and water for 3 whistles.",
            "Mash lentils slightly and add more water if too thick.",
            "For tadka: heat ghee in a small pan; add cumin seeds until they splutter.",
            "Add chopped garlic and dried chili; fry until golden.",
            "Add onion and tomato; cook until soft.",
            "Pour tadka over cooked lentils and stir.",
            "Squeeze lemon, garnish with coriander and serve with rice or roti."
        ],
        "cooking_time": "30 minutes",
        "calories"    : 250,
        "tags"        : ["indian", "veg", "dal", "lentils"]
    },

    "aloo_gobi": {
        "name"        : "Aloo Gobi",
        "emoji"       : "🥔",
        "category"    : "veg",
        "ingredients" : ["potato", "cauliflower", "onion", "tomato", "garlic",
                         "ginger", "cumin", "turmeric", "coriander powder",
                         "chili powder", "oil", "salt", "coriander leaves"],
        "steps"       : [
            "Cut potato and cauliflower into medium florets.",
            "Heat oil; add cumin seeds and let them splutter.",
            "Sauté onion until translucent; add garlic-ginger paste.",
            "Add all spices and tomatoes; cook until oil separates.",
            "Add potato; cook covered 5 minutes.",
            "Add cauliflower; stir well and cook covered 15 minutes on medium-low.",
            "Garnish with fresh coriander and serve with roti."
        ],
        "cooking_time": "35 minutes",
        "calories"    : 200,
        "tags"        : ["indian", "veg", "potato", "cauliflower"]
    },

    "samosa": {
        "name"        : "Samosa",
        "emoji"       : "🥟",
        "category"    : "veg",
        "ingredients" : ["flour", "potato", "peas", "onion", "ginger",
                         "cumin seeds", "coriander", "garam masala",
                         "chili", "oil", "salt", "water"],
        "steps"       : [
            "Make dough with flour, oil, salt and water; rest 20 minutes.",
            "Boil and mash potatoes; mix with peas, spices and coriander.",
            "Divide dough into balls; roll each into an oval.",
            "Cut oval in half; form a cone and fill with potato mixture.",
            "Seal edges with water; ensure no gaps.",
            "Deep fry in medium-hot oil until golden and crispy (8–10 min).",
            "Serve hot with mint chutney or tamarind sauce."
        ],
        "cooking_time": "45 minutes",
        "calories"    : 180,
        "tags"        : ["indian", "snack", "veg", "fried"]
    },

    "paneer_tikka": {
        "name"        : "Paneer Tikka",
        "emoji"       : "🧀",
        "category"    : "veg",
        "ingredients" : ["paneer", "yogurt", "bell pepper", "onion", "tomato",
                         "garlic", "ginger", "tikka masala", "turmeric",
                         "chili powder", "lemon", "oil", "salt"],
        "steps"       : [
            "Cut paneer, bell pepper, onion and tomato into cubes.",
            "Mix yogurt with all spices, garlic-ginger paste, lemon juice and oil.",
            "Marinate paneer and vegetables in the mix for at least 30 minutes.",
            "Thread onto skewers alternating paneer and vegetables.",
            "Grill or bake at 220°C for 15–18 minutes, turning halfway.",
            "Brush with butter and grill 2 more minutes for char.",
            "Serve with mint chutney and sliced onion rings."
        ],
        "cooking_time": "45 minutes",
        "calories"    : 290,
        "tags"        : ["indian", "veg", "paneer", "grilled", "starter"]
    },

    "chole_bhature": {
        "name"        : "Chole Bhature",
        "emoji"       : "🫙",
        "category"    : "veg",
        "ingredients" : ["chickpeas", "onion", "tomato", "garlic", "ginger",
                         "chana masala", "turmeric", "cumin", "bay leaf",
                         "flour", "yogurt", "baking soda", "oil", "salt"],
        "steps"       : [
            "Soak chickpeas overnight; pressure cook until soft.",
            "For bhature: mix flour, yogurt, baking soda and salt into a soft dough; rest 2 hours.",
            "Sauté onions until deep brown; add garlic-ginger and spices.",
            "Add blended tomatoes; cook until oil separates.",
            "Add cooked chickpeas and water; simmer 15 minutes.",
            "Roll bhature dough into thick circles; deep fry until puffed and golden.",
            "Serve hot chole with bhature and pickled onion."
        ],
        "cooking_time": "1 hour (+ overnight soak)",
        "calories"    : 580,
        "tags"        : ["indian", "veg", "chickpeas", "punjabi"]
    },

    "masala_dosa": {
        "name"        : "Masala Dosa",
        "emoji"       : "🫓",
        "category"    : "veg",
        "ingredients" : ["rice", "urad dal", "potato", "onion", "mustard seeds",
                         "curry leaves", "green chili", "turmeric", "ginger",
                         "oil", "salt", "chana dal"],
        "steps"       : [
            "Soak rice and urad dal separately for 6 hours; grind and ferment batter overnight.",
            "Boil and mash potatoes; prepare filling with mustard seeds, onion, chili, turmeric.",
            "Heat a flat tawa; pour a ladle of batter and spread in circles.",
            "Drizzle oil on the edges; cook until crispy and golden underneath.",
            "Place potato filling in the centre; fold dosa over the filling.",
            "Serve hot with coconut chutney and sambar."
        ],
        "cooking_time": "30 minutes (+ fermentation)",
        "calories"    : 340,
        "tags"        : ["indian", "veg", "south indian", "dosa", "breakfast"]
    },

    "gulab_jamun": {
        "name"        : "Gulab Jamun",
        "emoji"       : "🍮",
        "category"    : "veg",
        "ingredients" : ["milk powder", "flour", "ghee", "baking soda", "milk",
                         "sugar", "water", "cardamom", "rose water", "saffron", "oil"],
        "steps"       : [
            "Mix milk powder, flour, baking soda, ghee; add milk gradually to make soft dough.",
            "Divide into small equal balls; ensure no cracks.",
            "Make sugar syrup: boil sugar, water, cardamom and rose water for 5 minutes.",
            "Deep fry balls in medium-low oil, stirring gently until dark brown.",
            "Immediately transfer fried balls into warm sugar syrup.",
            "Soak for at least 30 minutes before serving.",
            "Serve warm or at room temperature; garnish with saffron."
        ],
        "cooking_time": "45 minutes",
        "calories"    : 380,
        "tags"        : ["indian", "dessert", "sweet", "veg"]
    },

    "rajma": {
        "name"        : "Rajma",
        "emoji"       : "🫘",
        "category"    : "veg",
        "ingredients" : ["kidney beans", "onion", "tomato", "garlic", "ginger",
                         "cumin", "coriander powder", "turmeric", "garam masala",
                         "chili powder", "oil", "salt", "coriander leaves"],
        "steps"       : [
            "Soak kidney beans overnight; pressure cook until very soft.",
            "Heat oil; sauté cumin seeds and onions until golden.",
            "Add garlic-ginger paste; cook 2 minutes.",
            "Add tomatoes and all spices; cook until oil separates.",
            "Add cooked beans with their liquid; mash some beans for thick gravy.",
            "Simmer 15 minutes; finish with garam masala.",
            "Garnish with coriander and serve with steamed rice."
        ],
        "cooking_time": "45 minutes (+ soak)",
        "calories"    : 280,
        "tags"        : ["indian", "veg", "beans", "punjabi"]
    },


    # ════════════════════════════════════════════════════════
    # 🇫🇷 FRENCH CUISINES (5)
    # ════════════════════════════════════════════════════════

    "french_onion_soup": {
        "name"        : "French Onion Soup",
        "emoji"       : "🧅",
        "category"    : "veg",
        "ingredients" : ["onion", "butter", "beef broth", "white wine", "flour",
                         "baguette", "gruyere cheese", "thyme", "bay leaf",
                         "salt", "pepper", "olive oil"],
        "steps"       : [
            "Slice onions thinly; caramelise in butter and olive oil on low heat for 40 minutes.",
            "Sprinkle flour over onions; stir and cook 2 minutes.",
            "Add white wine; cook until evaporated.",
            "Pour in broth; add thyme and bay leaf; simmer 20 minutes.",
            "Ladle soup into oven-safe bowls.",
            "Float baguette slices on top; pile on grated gruyere.",
            "Grill under broiler 3–4 minutes until cheese is bubbly and golden."
        ],
        "cooking_time": "1 hour 10 minutes",
        "calories"    : 310,
        "tags"        : ["french", "soup", "veg", "cheese"]
    },

    "ratatouille": {
        "name"        : "Ratatouille",
        "emoji"       : "🫑",
        "category"    : "veg",
        "ingredients" : ["zucchini", "eggplant", "bell pepper", "tomato", "onion",
                         "garlic", "olive oil", "thyme", "basil", "salt", "pepper"],
        "steps"       : [
            "Dice all vegetables into similar-sized pieces.",
            "Heat olive oil; sauté onion and garlic until soft.",
            "Add bell pepper and eggplant; cook 5 minutes.",
            "Add zucchini and tomatoes; stir in thyme and basil.",
            "Season well; simmer covered on low heat for 30 minutes.",
            "Uncover and cook another 10 minutes to reduce liquid.",
            "Serve warm or at room temperature as a side or main."
        ],
        "cooking_time": "55 minutes",
        "calories"    : 150,
        "tags"        : ["french", "veg", "stew", "healthy"]
    },

    "quiche_lorraine": {
        "name"        : "Quiche Lorraine",
        "emoji"       : "🥧",
        "category"    : "non-veg",
        "ingredients" : ["shortcrust pastry", "bacon", "eggs", "cream",
                         "gruyere cheese", "onion", "butter", "nutmeg", "salt", "pepper"],
        "steps"       : [
            "Press pastry into a tart tin; prick base and blind bake at 180°C for 15 minutes.",
            "Fry bacon and onion in butter until cooked; spread over pastry base.",
            "Whisk eggs, cream, nutmeg, salt and pepper.",
            "Pour egg mixture over bacon; sprinkle gruyere on top.",
            "Bake at 180°C for 30–35 minutes until set and golden.",
            "Cool slightly before slicing; serve warm or cold."
        ],
        "cooking_time": "1 hour",
        "calories"    : 420,
        "tags"        : ["french", "non-veg", "baked", "quiche"]
    },

    "beef_bourguignon": {
        "name"        : "Beef Bourguignon",
        "emoji"       : "🥩",
        "category"    : "non-veg",
        "ingredients" : ["beef", "red wine", "bacon", "mushroom", "carrot",
                         "onion", "garlic", "tomato paste", "beef broth",
                         "thyme", "bay leaf", "butter", "flour", "salt", "pepper"],
        "steps"       : [
            "Cut beef into chunks; season and brown in batches; set aside.",
            "Fry bacon; sauté onion, carrot and garlic in the same pot.",
            "Sprinkle flour and stir 1 minute.",
            "Pour in wine and broth; add tomato paste, thyme and bay leaf.",
            "Return beef to pot; bring to simmer.",
            "Cover and cook in oven at 160°C for 2.5 hours.",
            "Sauté mushrooms in butter; add to stew in last 30 minutes.",
            "Serve over mashed potatoes or egg noodles."
        ],
        "cooking_time": "3 hours",
        "calories"    : 510,
        "tags"        : ["french", "non-veg", "stew", "beef"]
    },

    "crepes": {
        "name"        : "French Crêpes",
        "emoji"       : "🥞",
        "category"    : "veg",
        "ingredients" : ["flour", "eggs", "milk", "butter", "sugar",
                         "vanilla", "salt", "lemon"],
        "steps"       : [
            "Whisk flour, eggs, milk, melted butter, sugar, vanilla and salt into smooth batter.",
            "Rest batter in fridge for 30 minutes.",
            "Heat a non-stick pan on medium; lightly butter it.",
            "Pour a thin layer of batter and swirl to coat the pan.",
            "Cook 1–2 minutes until edges lift; flip and cook 30 seconds.",
            "Repeat with remaining batter.",
            "Serve with lemon juice and sugar, Nutella, or fresh berries."
        ],
        "cooking_time": "45 minutes",
        "calories"    : 190,
        "tags"        : ["french", "veg", "sweet", "breakfast", "crepes"]
    },


    # ════════════════════════════════════════════════════════
    # 🇨🇳 CHINESE CUISINES (3)
    # ════════════════════════════════════════════════════════

    "kung_pao_chicken": {
        "name"        : "Kung Pao Chicken",
        "emoji"       : "🐔",
        "category"    : "non-veg",
        "ingredients" : ["chicken", "peanuts", "bell pepper", "dried chili",
                         "garlic", "ginger", "soy sauce", "rice vinegar",
                         "sugar", "cornstarch", "sesame oil", "oil", "green onion"],
        "steps"       : [
            "Cut chicken into cubes; marinate with soy sauce and cornstarch.",
            "Mix sauce: soy sauce, rice vinegar, sugar and sesame oil.",
            "Heat oil in wok; fry dried chilies and Sichuan pepper 30 seconds.",
            "Add chicken; stir-fry until golden and cooked through.",
            "Add garlic, ginger, bell pepper; stir-fry 2 minutes.",
            "Pour in sauce; toss everything together.",
            "Add peanuts and green onion; serve immediately over rice."
        ],
        "cooking_time": "25 minutes",
        "calories"    : 380,
        "tags"        : ["chinese", "non-veg", "spicy", "stir fry"]
    },

    "dim_sum": {
        "name"        : "Steamed Dim Sum (Har Gow)",
        "emoji"       : "🥟",
        "category"    : "non-veg",
        "ingredients" : ["shrimp", "wheat starch", "tapioca starch", "water",
                         "bamboo shoots", "sesame oil", "soy sauce",
                         "ginger", "salt", "sugar", "white pepper"],
        "steps"       : [
            "Mix wheat starch and tapioca starch; pour boiling water and stir rapidly.",
            "Knead into a smooth dough; rest 10 minutes.",
            "Chop shrimp and bamboo shoots; season with soy sauce, sesame oil and ginger.",
            "Roll dough thin; cut into circles.",
            "Place filling in centre; pleat and seal each dumpling.",
            "Steam in a bamboo steamer for 8–10 minutes.",
            "Serve hot with soy sauce and chili oil."
        ],
        "cooking_time": "45 minutes",
        "calories"    : 220,
        "tags"        : ["chinese", "non-veg", "steamed", "dumplings"]
    },

    "mapo_tofu": {
        "name"        : "Mapo Tofu",
        "emoji"       : "🍲",
        "category"    : "non-veg",
        "ingredients" : ["tofu", "ground pork", "doubanjiang", "garlic", "ginger",
                         "soy sauce", "chicken broth", "cornstarch",
                         "sesame oil", "green onion", "sichuan pepper", "oil"],
        "steps"       : [
            "Cut tofu into cubes; blanch in salted water 2 minutes; drain.",
            "Heat oil; fry ground pork until browned.",
            "Add doubanjiang (spicy bean paste); stir-fry 1 minute until fragrant.",
            "Add garlic and ginger; cook 30 seconds.",
            "Pour in broth and soy sauce; bring to simmer.",
            "Add tofu gently; simmer 5 minutes.",
            "Thicken with cornstarch slurry; finish with sesame oil, Sichuan pepper and green onion."
        ],
        "cooking_time": "25 minutes",
        "calories"    : 290,
        "tags"        : ["chinese", "non-veg", "tofu", "spicy"]
    },


    # ════════════════════════════════════════════════════════
    # 🇰🇷 KOREAN CUISINES (3)
    # ════════════════════════════════════════════════════════

    "bibimbap": {
        "name"        : "Bibimbap",
        "emoji"       : "🍱",
        "category"    : "veg",
        "ingredients" : ["rice", "spinach", "carrot", "zucchini", "mushroom",
                         "egg", "gochujang", "sesame oil", "soy sauce",
                         "garlic", "sesame seeds", "oil", "salt"],
        "steps"       : [
            "Cook rice; keep warm.",
            "Blanch spinach; squeeze dry and season with sesame oil, garlic and salt.",
            "Sauté carrot, zucchini and mushroom separately with soy sauce.",
            "Fry egg sunny-side up.",
            "Place rice in a bowl; arrange vegetables in sections on top.",
            "Place egg in the centre; add a spoonful of gochujang.",
            "Drizzle sesame oil and sprinkle sesame seeds; mix everything before eating."
        ],
        "cooking_time": "35 minutes",
        "calories"    : 420,
        "tags"        : ["korean", "veg", "rice bowl", "bibimbap"]
    },

    "tteokbokki": {
        "name"        : "Tteokbokki",
        "emoji"       : "🍢",
        "category"    : "veg",
        "ingredients" : ["rice cakes", "gochujang", "gochugaru", "soy sauce",
                         "sugar", "fish cake", "green onion", "sesame seeds",
                         "water", "garlic"],
        "steps"       : [
            "Soak rice cakes in cold water 15 minutes if hard.",
            "Mix gochujang, gochugaru, soy sauce, sugar and garlic into a paste.",
            "Bring water to boil; add the spice paste and stir.",
            "Add rice cakes and fish cakes; cook on medium 8–10 minutes.",
            "Sauce should thicken and coat the rice cakes.",
            "Add green onion in final minute.",
            "Sprinkle sesame seeds and serve hot."
        ],
        "cooking_time": "20 minutes",
        "calories"    : 330,
        "tags"        : ["korean", "spicy", "street food", "veg"]
    },

    "korean_fried_chicken": {
        "name"        : "Korean Fried Chicken",
        "emoji"       : "🍗",
        "category"    : "non-veg",
        "ingredients" : ["chicken", "flour", "cornstarch", "garlic powder",
                         "gochujang", "soy sauce", "honey", "rice vinegar",
                         "garlic", "ginger", "sesame oil", "oil", "salt", "pepper"],
        "steps"       : [
            "Cut chicken into pieces; season with salt, pepper, garlic powder.",
            "Coat in cornstarch and flour mixture; shake off excess.",
            "First fry at 160°C for 8 minutes; drain and rest.",
            "Second fry at 190°C for 3–4 minutes until very crispy.",
            "Make sauce: simmer gochujang, soy sauce, honey, vinegar, garlic and ginger.",
            "Toss fried chicken in the sauce.",
            "Garnish with sesame seeds and green onion; serve immediately."
        ],
        "cooking_time": "40 minutes",
        "calories"    : 480,
        "tags"        : ["korean", "non-veg", "fried", "chicken"]
    },


    # ════════════════════════════════════════════════════════
    # 🇯🇵 JAPANESE CUISINES (3)
    # ════════════════════════════════════════════════════════

    "chicken_ramen": {
        "name"        : "Chicken Ramen",
        "emoji"       : "🍜",
        "category"    : "non-veg",
        "ingredients" : ["ramen noodles", "chicken", "soy sauce", "mirin",
                         "chicken broth", "garlic", "ginger", "soft boiled egg",
                         "green onion", "nori", "sesame oil", "salt", "pepper"],
        "steps"       : [
            "Simmer chicken broth with garlic, ginger, soy sauce and mirin for 20 minutes.",
            "Cook chicken thigh in the broth until done; slice thinly.",
            "Boil eggs 6.5 minutes; cool in ice water and peel; halve.",
            "Cook ramen noodles according to package; drain.",
            "Ladle hot broth into a bowl; add noodles.",
            "Arrange chicken slices, egg halves and nori on top.",
            "Drizzle sesame oil; garnish with sliced green onion."
        ],
        "cooking_time": "40 minutes",
        "calories"    : 480,
        "tags"        : ["japanese", "non-veg", "noodles", "soup", "ramen"]
    },

    "sushi_rolls": {
        "name"        : "Vegetable Sushi Rolls",
        "emoji"       : "🍣",
        "category"    : "veg",
        "ingredients" : ["sushi rice", "nori", "cucumber", "avocado",
                         "carrot", "rice vinegar", "sugar", "salt",
                         "soy sauce", "wasabi", "pickled ginger"],
        "steps"       : [
            "Cook sushi rice; season with rice vinegar, sugar and salt while warm.",
            "Place nori shiny side down on a bamboo mat.",
            "Spread a thin, even layer of rice over nori, leaving 1-inch at top.",
            "Arrange cucumber, avocado and carrot strips in a row near the bottom.",
            "Roll tightly using the mat, pressing firmly.",
            "Wet the exposed nori edge to seal; press and hold.",
            "Cut into 6–8 pieces with a wet knife; serve with soy sauce and wasabi."
        ],
        "cooking_time": "40 minutes",
        "calories"    : 220,
        "tags"        : ["japanese", "veg", "sushi", "rice"]
    },

    "miso_soup": {
        "name"        : "Miso Soup",
        "emoji"       : "🍵",
        "category"    : "veg",
        "ingredients" : ["miso paste", "tofu", "dashi stock", "wakame seaweed",
                         "green onion", "water", "soy sauce"],
        "steps"       : [
            "Bring dashi stock to a gentle simmer (do not boil).",
            "Rehydrate wakame seaweed in cold water for 5 minutes; drain.",
            "Cut tofu into small cubes.",
            "Dissolve miso paste in a small amount of warm broth; stir back into pot.",
            "Add tofu and seaweed; heat gently for 2 minutes.",
            "Do not let soup boil after adding miso — it destroys the flavour.",
            "Ladle into bowls; garnish with sliced green onion."
        ],
        "cooking_time": "15 minutes",
        "calories"    : 80,
        "tags"        : ["japanese", "veg", "soup", "quick", "miso"]
    },


    # ════════════════════════════════════════════════════════
    # 🇪🇸 SPANISH CUISINES (3)
    # ════════════════════════════════════════════════════════

    "paella": {
        "name"        : "Chicken & Seafood Paella",
        "emoji"       : "🥘",
        "category"    : "non-veg",
        "ingredients" : ["paella rice", "chicken", "shrimp", "mussels", "onion",
                         "bell pepper", "tomato", "garlic", "saffron",
                         "chicken broth", "smoked paprika", "olive oil", "salt", "lemon"],
        "steps"       : [
            "Heat olive oil in a wide paella pan; brown chicken pieces; set aside.",
            "Sauté onion, garlic and bell pepper until soft.",
            "Add tomatoes and smoked paprika; cook 3 minutes.",
            "Add rice; stir to coat with the sofrito.",
            "Pour in hot saffron-infused broth; add chicken back.",
            "Cook uncovered on medium 10 minutes; DO NOT stir.",
            "Add shrimp and mussels; cook another 8 minutes until seafood is done.",
            "Rest 5 minutes; serve with lemon wedges."
        ],
        "cooking_time": "50 minutes",
        "calories"    : 520,
        "tags"        : ["spanish", "non-veg", "rice", "seafood", "paella"]
    },

    "gazpacho": {
        "name"        : "Gazpacho",
        "emoji"       : "🍅",
        "category"    : "veg",
        "ingredients" : ["tomato", "cucumber", "bell pepper", "onion", "garlic",
                         "olive oil", "red wine vinegar", "bread", "salt", "pepper"],
        "steps"       : [
            "Roughly chop tomatoes, cucumber, bell pepper and onion.",
            "Soak a slice of stale bread in water for 5 minutes; squeeze dry.",
            "Blend all vegetables with garlic, bread and a splash of water until smooth.",
            "Add olive oil and red wine vinegar; blend again.",
            "Season generously with salt and pepper.",
            "Chill in the refrigerator for at least 2 hours.",
            "Serve cold with a drizzle of olive oil and diced toppings."
        ],
        "cooking_time": "15 minutes (+ 2 hr chill)",
        "calories"    : 120,
        "tags"        : ["spanish", "veg", "soup", "cold", "healthy"]
    },

    "patatas_bravas": {
        "name"        : "Patatas Bravas",
        "emoji"       : "🥔",
        "category"    : "veg",
        "ingredients" : ["potato", "olive oil", "smoked paprika", "garlic",
                         "tomato", "onion", "chili flakes", "mayonnaise",
                         "salt", "pepper", "vinegar"],
        "steps"       : [
            "Cut potatoes into rough 2cm cubes; toss with olive oil and salt.",
            "Roast at 220°C for 30–35 minutes until crispy and golden.",
            "For bravas sauce: sauté onion and garlic; add tomato, smoked paprika and chili.",
            "Simmer sauce 10 minutes; blend smooth; season with vinegar and salt.",
            "For aioli: mix mayonnaise with crushed garlic and a squeeze of lemon.",
            "Pile potatoes on a plate; drizzle generously with both sauces.",
            "Serve immediately as a tapas."
        ],
        "cooking_time": "45 minutes",
        "calories"    : 290,
        "tags"        : ["spanish", "veg", "tapas", "potato", "snack"]
    },


    # ════════════════════════════════════════════════════════
    # 🍰 DESSERTS (5)
    # ════════════════════════════════════════════════════════

    "chocolate_lava_cake": {
        "name"        : "Chocolate Lava Cake",
        "emoji"       : "🍫",
        "category"    : "veg",
        "ingredients" : ["dark chocolate", "butter", "eggs", "sugar",
                         "flour", "vanilla", "salt", "powdered sugar"],
        "steps"       : [
            "Preheat oven to 220°C; grease and flour four ramekins.",
            "Melt chocolate and butter together; cool slightly.",
            "Whisk eggs, egg yolks and sugar until pale and thick.",
            "Fold chocolate mixture into eggs; sift in flour and salt.",
            "Pour batter into ramekins; refrigerate up to 24 hours at this point.",
            "Bake 12 minutes — edges firm, centre jiggles slightly.",
            "Invert onto plates; dust with powdered sugar and serve immediately."
        ],
        "cooking_time": "25 minutes",
        "calories"    : 410,
        "tags"        : ["dessert", "chocolate", "baked", "veg"]
    },

    "tiramisu": {
        "name"        : "Tiramisu",
        "emoji"       : "☕",
        "category"    : "veg",
        "ingredients" : ["ladyfinger biscuits", "mascarpone", "eggs", "sugar",
                         "espresso", "cocoa powder", "heavy cream", "vanilla", "salt"],
        "steps"       : [
            "Brew strong espresso; cool to room temperature.",
            "Separate eggs; whisk yolks with sugar until pale.",
            "Fold in mascarpone until smooth.",
            "Whip heavy cream to stiff peaks; fold gently into mascarpone mixture.",
            "Quickly dip ladyfingers in espresso (don't soak); layer in dish.",
            "Spread half the cream mixture; repeat with another layer of biscuits.",
            "Top with remaining cream; dust generously with cocoa powder.",
            "Refrigerate at least 4 hours or overnight before serving."
        ],
        "cooking_time": "30 minutes (+ 4 hr chill)",
        "calories"    : 360,
        "tags"        : ["dessert", "italian", "no-bake", "veg"]
    },

    "mango_sorbet": {
        "name"        : "Mango Sorbet",
        "emoji"       : "🥭",
        "category"    : "veg",
        "ingredients" : ["mango", "sugar", "water", "lemon juice"],
        "steps"       : [
            "Make simple syrup: boil sugar and water until dissolved; cool.",
            "Peel and blend ripe mango until completely smooth.",
            "Mix mango purée with syrup and lemon juice.",
            "Taste and adjust sweetness.",
            "Pour into a shallow container; freeze 2 hours.",
            "Scrape with a fork; return to freezer for 1 hour.",
            "Repeat scraping once more; serve scooped in chilled glasses."
        ],
        "cooking_time": "20 minutes (+ 3 hr freeze)",
        "calories"    : 140,
        "tags"        : ["dessert", "veg", "frozen", "fruit", "healthy"]
    },

    "cheesecake": {
        "name"        : "New York Cheesecake",
        "emoji"       : "🍰",
        "category"    : "veg",
        "ingredients" : ["cream cheese", "sugar", "eggs", "sour cream",
                         "vanilla", "digestive biscuits", "butter", "lemon zest", "salt"],
        "steps"       : [
            "Crush biscuits; mix with melted butter; press into springform tin base.",
            "Chill base 15 minutes in freezer.",
            "Beat cream cheese and sugar until smooth.",
            "Add eggs one at a time; mix in sour cream, vanilla, lemon zest and salt.",
            "Pour over base; smooth the top.",
            "Bake in a water bath at 160°C for 55–60 minutes until set with slight wobble.",
            "Cool in oven with door ajar 1 hour; refrigerate overnight.",
            "Slice with a warm knife and serve plain or with berry coulis."
        ],
        "cooking_time": "1 hour 20 minutes (+ overnight chill)",
        "calories"    : 440,
        "tags"        : ["dessert", "baked", "veg", "cheesecake"]
    },

    "kheer": {
        "name"        : "Kheer (Rice Pudding)",
        "emoji"       : "🍚",
        "category"    : "veg",
        "ingredients" : ["rice", "full fat milk", "sugar", "cardamom",
                         "saffron", "cashews", "raisins", "rose water", "ghee"],
        "steps"       : [
            "Wash rice; soak 20 minutes.",
            "Bring milk to boil in a heavy pan; add drained rice.",
            "Simmer on low, stirring frequently, for 30–35 minutes until thick.",
            "Add sugar, cardamom powder and saffron; stir well.",
            "Fry cashews and raisins in ghee; add to kheer.",
            "Add a splash of rose water; stir.",
            "Serve warm or chilled; garnish with extra nuts."
        ],
        "cooking_time": "45 minutes",
        "calories"    : 300,
        "tags"        : ["indian", "dessert", "sweet", "veg", "kheer"]
    },


    # ════════════════════════════════════════════════════════
    # 🥤 DRINKS (5)
    # ════════════════════════════════════════════════════════

    "mango_lassi": {
        "name"        : "Mango Lassi",
        "emoji"       : "🥭",
        "category"    : "veg",
        "ingredients" : ["mango", "yogurt", "milk", "sugar", "cardamom", "ice"],
        "steps"       : [
            "Peel and dice ripe mango.",
            "Add mango, yogurt, milk, sugar and cardamom to a blender.",
            "Blend until completely smooth and frothy.",
            "Taste and adjust sweetness.",
            "Add ice cubes; blend briefly.",
            "Pour into tall glasses; sprinkle a pinch of cardamom on top.",
            "Serve immediately."
        ],
        "cooking_time": "5 minutes",
        "calories"    : 180,
        "tags"        : ["drink", "indian", "veg", "smoothie", "mango"]
    },

    "masala_chai": {
        "name"        : "Masala Chai",
        "emoji"       : "🫖",
        "category"    : "veg",
        "ingredients" : ["black tea", "milk", "water", "ginger", "cardamom",
                         "cinnamon", "cloves", "black pepper", "sugar"],
        "steps"       : [
            "Crush ginger, cardamom pods, cinnamon and cloves coarsely.",
            "Bring water to boil; add crushed spices and ginger.",
            "Simmer 3 minutes to extract flavours.",
            "Add tea leaves; boil 1 minute.",
            "Pour in milk; bring back to boil, then reduce heat.",
            "Simmer 3 minutes until chai turns a rich golden colour.",
            "Strain into cups; sweeten to taste and serve hot."
        ],
        "cooking_time": "10 minutes",
        "calories"    : 90,
        "tags"        : ["drink", "indian", "veg", "hot", "chai", "tea"]
    },

    "lemonade": {
        "name"        : "Classic Lemonade",
        "emoji"       : "🍋",
        "category"    : "veg",
        "ingredients" : ["lemon", "sugar", "water", "mint", "ice"],
        "steps"       : [
            "Make simple syrup: heat ½ cup sugar with ½ cup water until dissolved; cool.",
            "Juice 4–6 lemons to get ¾ cup of juice.",
            "Combine lemon juice, syrup and 3 cups cold water; stir well.",
            "Taste and adjust — add more syrup or lemon as needed.",
            "Fill glasses with ice; pour lemonade.",
            "Garnish with lemon slices and fresh mint."
        ],
        "cooking_time": "10 minutes",
        "calories"    : 100,
        "tags"        : ["drink", "veg", "cold", "refreshing", "lemonade"]
    },

    "strawberry_smoothie": {
        "name"        : "Strawberry Banana Smoothie",
        "emoji"       : "🍓",
        "category"    : "veg",
        "ingredients" : ["strawberry", "banana", "yogurt", "milk", "honey", "ice"],
        "steps"       : [
            "Hull and halve fresh strawberries.",
            "Peel and slice banana.",
            "Add all ingredients to a blender.",
            "Blend on high until completely smooth.",
            "Taste and add more honey if desired.",
            "Pour into glasses and serve immediately."
        ],
        "cooking_time": "5 minutes",
        "calories"    : 160,
        "tags"        : ["drink", "veg", "smoothie", "healthy", "fruit"]
    },

    "cold_coffee": {
        "name"        : "Cold Coffee",
        "emoji"       : "☕",
        "category"    : "veg",
        "ingredients" : ["instant coffee", "milk", "sugar", "ice cream",
                         "ice", "vanilla", "whipped cream"],
        "steps"       : [
            "Dissolve instant coffee and sugar in 2 tbsp hot water.",
            "Add milk, ice cream, ice and vanilla to a blender.",
            "Add the coffee mixture.",
            "Blend until frothy and smooth.",
            "Pour into tall glasses.",
            "Top with whipped cream and a dusting of coffee powder.",
            "Serve immediately with a straw."
        ],
        "cooking_time": "5 minutes",
        "calories"    : 220,
        "tags"        : ["drink", "veg", "cold", "coffee", "sweet"]
    },


    # ════════════════════════════════════════════════════════
    # 🍿 SNACKS (5)
    # ════════════════════════════════════════════════════════

    "bruschetta": {
        "name"        : "Bruschetta",
        "emoji"       : "🥖",
        "category"    : "veg",
        "ingredients" : ["baguette", "tomato", "garlic", "basil",
                         "olive oil", "salt", "pepper", "balsamic vinegar"],
        "steps"       : [
            "Slice baguette diagonally into thick pieces.",
            "Toast slices under a grill or in a pan until golden.",
            "Rub each slice with a cut garlic clove while still warm.",
            "Dice tomatoes; mix with torn basil, olive oil, salt and pepper.",
            "Pile tomato mixture on each slice.",
            "Drizzle with balsamic vinegar.",
            "Serve immediately so bread stays crispy."
        ],
        "cooking_time": "15 minutes",
        "calories"    : 160,
        "tags"        : ["snack", "italian", "veg", "quick", "starter"]
    },

    "cheese_quesadilla": {
        "name"        : "Cheese Quesadilla",
        "emoji"       : "🫓",
        "category"    : "veg",
        "ingredients" : ["flour tortilla", "cheddar cheese", "bell pepper",
                         "onion", "jalapeño", "sour cream", "butter", "salt"],
        "steps"       : [
            "Dice bell pepper, onion and jalapeño finely.",
            "Butter one side of each tortilla.",
            "Place one tortilla buttered side down in a pan.",
            "Scatter cheese and vegetables over one half.",
            "Fold the empty half over the filled side.",
            "Cook on medium heat 2–3 minutes until golden; flip carefully.",
            "Cook another 2 minutes; slice into wedges and serve with sour cream."
        ],
        "cooking_time": "15 minutes",
        "calories"    : 350,
        "tags"        : ["snack", "mexican", "veg", "quick", "cheese"]
    },

    "hummus_and_pita": {
        "name"        : "Hummus with Pita Chips",
        "emoji"       : "🫘",
        "category"    : "veg",
        "ingredients" : ["chickpeas", "tahini", "lemon", "garlic",
                         "olive oil", "cumin", "salt", "pita bread", "paprika"],
        "steps"       : [
            "Drain chickpeas; reserve a few for garnish.",
            "Blend chickpeas with tahini, lemon juice, garlic, cumin and salt.",
            "Add ice cold water gradually until smooth and creamy.",
            "Taste and adjust seasoning.",
            "Cut pita bread into triangles; bake at 200°C for 8 minutes until crispy.",
            "Spread hummus in a shallow bowl; make a well in the centre.",
            "Fill well with olive oil; sprinkle paprika and reserved chickpeas."
        ],
        "cooking_time": "20 minutes",
        "calories"    : 280,
        "tags"        : ["snack", "veg", "healthy", "middle eastern", "dip"]
    },

    "spring_rolls": {
        "name"        : "Crispy Spring Rolls",
        "emoji"       : "🥢",
        "category"    : "veg",
        "ingredients" : ["spring roll wrappers", "cabbage", "carrot", "mushroom",
                         "glass noodles", "garlic", "ginger", "soy sauce",
                         "sesame oil", "oil", "cornstarch", "salt", "pepper"],
        "steps"       : [
            "Soak glass noodles in hot water 5 minutes; drain and chop.",
            "Shred cabbage and carrot; slice mushrooms.",
            "Stir-fry garlic, ginger, vegetables and noodles with soy sauce.",
            "Season with sesame oil, salt and pepper; cool completely.",
            "Place filling on a wrapper; fold sides in and roll tightly.",
            "Seal edge with cornstarch paste.",
            "Deep fry in hot oil until golden and very crispy (3–4 minutes).",
            "Drain and serve with sweet chili sauce."
        ],
        "cooking_time": "35 minutes",
        "calories"    : 200,
        "tags"        : ["snack", "asian", "veg", "fried", "party"]
    },

    "deviled_eggs": {
        "name"        : "Deviled Eggs",
        "emoji"       : "🥚",
        "category"    : "veg",
        "ingredients" : ["eggs", "mayonnaise", "mustard", "vinegar",
                         "paprika", "salt", "pepper", "chives"],
        "steps"       : [
            "Hard boil eggs 10 minutes; cool in ice water and peel.",
            "Halve eggs lengthwise; scoop out yolks into a bowl.",
            "Mash yolks with mayonnaise, mustard, vinegar, salt and pepper.",
            "Mix until completely smooth; taste and adjust seasoning.",
            "Pipe or spoon filling back into egg white halves.",
            "Dust with paprika; garnish with snipped chives.",
            "Refrigerate until ready to serve."
        ],
        "cooking_time": "20 minutes",
        "calories"    : 140,
        "tags"        : ["snack", "veg", "party", "eggs", "quick"]
    },
}


# ─────────────────────────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────────────────────────

def get_recipe_by_id(recipe_id: str) -> dict | None:
    return RECIPE_DATABASE.get(recipe_id, None)


def get_all_recipes() -> list:
    return [{"id": rid, **recipe} for rid, recipe in RECIPE_DATABASE.items()]


def get_recipe_count() -> int:
    return len(RECIPE_DATABASE)
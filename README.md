# 🍳 AI Recipe Generator — Backend

Flask + SQLite backend that stores dish name, ingredients, dietary preference, and allergy information.

---

## 🚀 Quick Start

```bash
pip install -r requirements.txt
python app.py
```

Visit **http://127.0.0.1:5000** — the database is created automatically.

---

## 🗃️ Database Schema

```
recipes
├── id                  INTEGER  (auto, primary key)
├── dish_name           TEXT     (required)
├── ingredients         TEXT     (required)
├── dietary_preference  TEXT     (required — e.g. Vegan, Vegetarian, Non-Vegetarian)
├── allergy_info        TEXT     (optional — e.g. "Contains gluten, dairy")
└── created_at          DATETIME (auto timestamp)
```

---

## 🔌 API Endpoints

| Method | URL | What it does |
|--------|-----|--------------|
| POST | `/recipes` | Save a new recipe |
| GET | `/recipes` | Get all recipes |
| GET | `/recipes/<id>` | Get one recipe by ID |
| GET | `/recipes/filter/diet?type=Vegan` | Filter by dietary preference |
| GET | `/recipes/filter/allergy?avoid=gluten` | Filter allergy-safe recipes |
| DELETE | `/recipes/<id>` | Delete a recipe |

---

## 🧪 Example — Save a recipe

```bash
curl -X POST http://127.0.0.1:5000/recipes \
     -H "Content-Type: application/json" \
     -d '{
       "dish_name": "Avocado Toast",
       "ingredients": "bread, avocado, lemon, salt, chili flakes",
       "dietary_preference": "Vegan",
       "allergy_info": "Contains gluten"
     }'
```

Response:
```json
{ "success": true, "message": "Recipe saved with ID 1.", "id": 1 }
```

---

## 📁 File Structure

```
recipe_backend/
├── app.py            ← Flask routes
├── database.py       ← DB connection & table setup
├── recipe_module.py  ← All database operations
├── requirements.txt
├── .gitignore
└── README.md
```

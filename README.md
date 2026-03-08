# 🥘 Ahava's Kitchen — AI Smart Recipe Generator

A smart, AI-powered recipe finder that matches recipes based on the ingredients you have at home.

🌐 **Live Site**: [aleenadon08.pythonanywhere.com](https://aleenadon08.pythonanywhere.com)

---

## ✨ Features

- 🔍 **Smart Recipe Search** — Enter ingredients you have and get matched recipes ranked by similarity
- 🌿 **Diet Aware** — Filter by vegetarian or non-vegetarian preference
- 🚫 **Allergy Filter** — Automatically exclude recipes with allergens
- 🔄 **Ingredient Substitutes** — Suggests smart swaps for missing ingredients
- ❤️ **Favourites** — Save your favourite recipes per user account
- 🕐 **Search History** — Tracks your recent searches
- 📝 **Kitchen Notes** — Personal notepad for cooking reminders
- 🔐 **User Authentication** — Register, login and logout securely

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask, Flask-Login
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **Auth**: bcrypt password hashing
- **Hosting**: PythonAnywhere

---

## 📁 Project Structure

```
Recipe/
├── App2.py                  # Main Flask app
├── database_setup.py        # Initialise auth database
├── auth_routes.py           # Login, register, logout routes
├── database.py              # Search history DB
├── modules/
│   ├── auth_module.py       # User authentication logic
│   ├── user_data_module.py  # Favourites, history, preferences
│   ├── recipe_database_module.py
│   ├── recommendation_module.py
│   ├── user_input_module.py
│   ├── output_module.py
│   └── substitute_module.py
├── templates/
│   ├── index.html           # Main app UI
│   └── login.html           # Login & Register page
└── static/
    ├── style.css
    └── images/
```

---

## 🚀 Run Locally

1. Clone the repo:
```bash
git clone https://github.com/Aleena-D-Bosco/Recipe.git
cd Recipe
```

2. Install dependencies:
```bash
pip install flask flask-login bcrypt
```

3. Initialise the database:
```bash
python database_setup.py
```

4. Run the app:
```bash
python App2.py
```

5. Visit `http://127.0.0.1:5000`

---

## 👩‍💻 Developed by

**Aleena D Bosco** — [GitHub](https://github.com/Aleena-D-Bosco)

# 🔐 RecipeAI – Auth & User Tracking Setup

Follow these steps to plug in login, search history, favourites, and preferences.

---

## 1. Install dependencies

```bash
pip install flask-login bcrypt
```

---

## 2. File placement

Put the new files in your project like this:

```
your-project/
├── app.py  (or App2.py)
├── database_setup.py          ← NEW
├── auth_routes.py             ← NEW
├── modules/
│   ├── auth_module.py         ← NEW
│   ├── user_data_module.py    ← NEW
│   ├── recipe_database_module.py
│   ├── recommendation_module.py
│   ├── user_input_module.py
│   └── output_module.py
├── templates/
│   ├── index.html
│   └── login.html             ← NEW
└── static/
    └── style.css
```

---

## 3. Initialise the database

Run this **once** before starting the app:

```bash
python database_setup.py
```

This creates `recipeai.db` with all tables: `users`, `user_preferences`, `search_history`, `favourites`.

---

## 4. Update your main app file (app.py / App2.py)

Add these lines:

```python
from flask_login import current_user, login_required
from auth_routes import auth_bp, init_login_manager
from database_setup import init_db

app = Flask(__name__)
app.secret_key = "change-this-to-something-secret"  # ← CHANGE THIS

# Register auth blueprint and login manager
app.register_blueprint(auth_bp)
init_login_manager(app)

# Initialise DB on startup
init_db()
```

---

## 5. Protect your main route

Add `@login_required` to your home route so only logged-in users can access it:

```python
@app.route("/")
@login_required
def index():
    return render_template("index.html")
```

---

## 6. Save searches to DB (in your /search route)

After getting results, save the search:

```python
from flask_login import current_user
from modules.user_data_module import save_search

# After computing results...
save_search(current_user.id, parsed_input, len(results))
```

---

## 7. What each new file does

| File | Purpose |
|------|---------|
| `database_setup.py` | Creates all SQLite tables |
| `modules/auth_module.py` | Register, login, fetch user logic |
| `modules/user_data_module.py` | Search history, favourites, preferences |
| `auth_routes.py` | Flask routes for login/register/logout + API endpoints |
| `templates/login.html` | Login & Register UI page |

---

## 8. Available API endpoints (called from JS)

| Endpoint | Method | What it does |
|----------|--------|--------------|
| `/login` | POST | Log in |
| `/register` | POST | Create account |
| `/logout` | GET | Log out |
| `/api/history` | GET | Get user's search history |
| `/api/history/clear` | POST | Clear history |
| `/api/favourites` | GET | Get favourites |
| `/api/favourites/add` | POST | Add a favourite |
| `/api/favourites/remove` | POST | Remove a favourite |
| `/api/preferences` | GET | Get dietary preferences |
| `/api/preferences/save` | POST | Update preferences |

---

## 9. Access current user in templates

In any template (index.html etc.) you can now use:

```html
<p>Hello, {{ current_user.username }}!</p>
```

And add a logout button to your sidebar:

```html
<a href="/logout" class="nav-item">
    <span class="nav-icon">🚪</span>
    <span>Logout</span>
</a>
```

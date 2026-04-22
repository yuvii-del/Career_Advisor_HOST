# Career & Educational Advisor - Django Backend

Django backend for the AI-powered Personalized Career & Educational Advisor Platform.

## Quick Start

```bash
# Create and activate virtual environment (recommended)
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt


# Run migrations (when models are added)
python manage.py migrate

# Start development server
python manage.py runserver
```

Visit: **http://127.0.0.1:8000/login/**

## URL Routes

| Route | Page |
|-------|------|
| `/` | Redirects to /login/ |
| `/login/` | Login / Landing (split screen) |
| `/profile-analysis/` | Student profile form |
| `/career-guidance/` | Career recommendations results |

## Project Structure

```
backend/
├── career_advisor/     # Project config
├── advisor/            # Main app
├── templates/          # Base + advisor templates
├── static/
│   ├── css/            # styles.css, login.css, profile.css, career.css
│   ├── fonts/          # Vijaya.ttf for Tamil PDF support (download separately)
│   └── js/
├── manage.py
└── requirements.txt
```



# Kynye Academy API

## Description
This is the backend API for Kynye Academy, built with Django REST Framework.

## Features
- JWT Authentication
- API Documentation with Swagger/ReDoc
- CORS support
- Environment variables configuration
- Production-ready settings
- Static files served with WhiteNoise

## Requirements
- Python 3.11+
- Django 5.2+
- PostgreSQL (optional, can use SQLite for development)

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/kynye_academy_api.git
cd kynye_academy_api
```

2. Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Copy .env.example to .env and update the variables
```bash
cp .env.example .env
```

5. Run migrations
```bash
python manage.py migrate
```

6. Create superuser
```bash
python manage.py createsuperuser
```

7. Run the development server
```bash
python manage.py runserver
```

## API Documentation
- Swagger UI: http://localhost:8000/
- ReDoc: http://localhost:8000/redoc/

## Authentication
The API uses JWT (JSON Web Token) authentication. To get a token:

```bash
curl -X POST http://localhost:8000/api/auth/token/ -d "username=admin&password=password"
```

## Project Structure
```
kynye_academy_api/
├── apps/               # Django applications
├── core/              # Project configuration
├── static/            # Static files
├── media/             # User uploaded files
├── templates/         # HTML templates
├── .env              # Environment variables
├── .gitignore        # Git ignore rules
├── manage.py         # Django's command-line utility
└── requirements.txt  # Project dependencies
```

## Development
1. Create a new app
```bash
python manage.py startapp app_name
```

2. Register the app in `INSTALLED_APPS`
3. Create models
4. Create serializers
5. Create views
6. Add URLs

## Testing
```bash
pytest
```

## Code Quality
```bash
# Format code
black .

# Sort imports
isort .

# Lint code
flake8
```

## Deployment
1. Update .env with production settings
2. Collect static files
```bash
python manage.py collectstatic
```
3. Run migrations
```bash
python manage.py migrate
```
4. Use gunicorn for production server
```bash
gunicorn core.wsgi:application
```

## License
This project is licensed under the terms of the MIT license.

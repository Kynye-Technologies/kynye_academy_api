# Kynye Academy API

## Description
Backend API for Kynye Academy, built with Django REST Framework, featuring a custom user model, hierarchical expertise, JWT/Djoser/social authentication, and robust test-driven development.

## Features
- Custom user model (email login, instructor/student types)
- JWT Authentication (SimpleJWT) & Djoser endpoints
- Social authentication (Google, Facebook, etc.)
- Hierarchical expertise structure (MainExpertise > Category > Specialization > Course)
- Instructor and student profiles with permissions
- Courses app with full CRUD and filtering
- API Documentation (Swagger/ReDoc)
- CORS support
- Environment variables configuration
- Production-ready settings
- Static files served with WhiteNoise
- PostgreSQL (with SQLite fallback for local/testing)
- Robust tests (pytest, factory_boy)
- GitHub Actions CI/CD with coverage reporting

## Requirements
- Python 3.11+
- Django 5.2+
- PostgreSQL (optional, SQLite for development/testing)

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
- JWT via Djoser: `/auth/jwt/create/`, `/auth/jwt/refresh/`, `/auth/users/`
- Social auth: `/auth/o/google-oauth2/`, `/auth/o/facebook/`, etc.

## Main Endpoints
- `/profiles/` — Instructor and student profiles
- `/courses/` — Courses CRUD, filtering by expertise/category/specialization

## Usage Examples

### Authentication
#### Obtain JWT Token
```bash
POST /auth/jwt/create/
{
  "email": "user@example.com",
  "password": "yourpassword"
}
```
Response:
```json
{
  "access": "<jwt-access-token>",
  "refresh": "<jwt-refresh-token>"
}
```

#### Social Auth Example (Google)
```bash
POST /auth/o/google-oauth2/?state=...&code=...
```

### Profiles
#### Get Current User Profile
```bash
GET /profiles/me/
Authorization: JWT <access-token>
```

#### Update Profile
```bash
PATCH /profiles/me/
{
  "bio": "Updated bio"
}
```

### Courses
#### List Courses
```bash
GET /courses/
```

#### Filter by Main Expertise
```bash
GET /courses/?main_expertise=Web Development
```

#### Create Course (Instructor Only)
```bash
POST /courses/
Authorization: JWT <access-token>
{
  "title": "New Course",
  "description": "A test course",
  "specialization": 1
}
```

#### Retrieve Course
```bash
GET /courses/1/
```

## API Endpoints Overview

| Endpoint                | Methods | Description                                 |
|------------------------|---------|---------------------------------------------|
| /auth/                 | POST    | Djoser auth (register, login, reset, etc.)  |
| /auth/jwt/create/      | POST    | Obtain JWT token                            |
| /auth/jwt/refresh/     | POST    | Refresh JWT token                           |
| /auth/o/<provider>/    | POST    | Social auth (Google, Facebook, etc.)        |
| /profiles/             | GET     | List all profiles (admin/instructor only)   |
| /profiles/me/          | GET     | Get current user's profile                  |
| /profiles/me/          | PATCH   | Update current user's profile               |
| /courses/              | GET     | List all courses                            |
| /courses/              | POST    | Create a new course (instructor only)       |
| /courses/<id>/         | GET     | Retrieve a course by ID                     |
| /courses/<id>/         | PATCH   | Update a course (instructor only)           |
| /courses/<id>/         | DELETE  | Delete a course (instructor only)           |

## Project Structure
```
kynye_academy_api/
├── apps/
│   ├── accounts/        # Custom user model, registration, auth
│   ├── profiles/        # Instructor/Student profiles, signals, permissions
│   └── courses/         # Hierarchical expertise, categories, courses
├── core/                # Project configuration, settings, urls
├── static/              # Static files
├── media/               # User uploaded files
├── templates/           # HTML templates
├── .env                 # Environment variables
├── .github/workflows/   # GitHub Actions CI/CD
├── manage.py            # Django's command-line utility
└── requirements.txt     # Project dependencies
```

## Testing & TDD
- All new features are developed with tests first (pytest, factory_boy)
- Run tests:  
```bash
pytest
```
- Coverage is reported in CI and locally (see GitHub Actions)

## Code Quality
```bash
# Format code
black .
# Sort imports
isort .
# Lint code
flake8
```

## CI/CD
- Automated tests and coverage via GitHub Actions (`.github/workflows/ci.yml`)
- PRs and pushes are checked for passing tests and minimum coverage

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

## Social Authentication Setup
This project supports login via Google, Facebook, GitHub, Twitter, and LinkedIn using [social-auth-app-django](https://python-social-auth.readthedocs.io/en/latest/).

### Environment Variables
Add the following to your `.env` file with your provider credentials:
```
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your-google-client-id
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your-google-client-secret
SOCIAL_AUTH_FACEBOOK_KEY=your-facebook-app-id
SOCIAL_AUTH_FACEBOOK_SECRET=your-facebook-app-secret
SOCIAL_AUTH_GITHUB_KEY=your-github-client-id
SOCIAL_AUTH_GITHUB_SECRET=your-github-client-secret
SOCIAL_AUTH_TWITTER_KEY=your-twitter-api-key
SOCIAL_AUTH_TWITTER_SECRET=your-twitter-api-secret
SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY=your-linkedin-client-id
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET=your-linkedin-client-secret
```

### Social Auth Endpoints
- `/auth/login/<provider>/` — Redirect to provider (browser)
- `/auth/complete/<provider>/` — Provider callback (browser)
- `/auth/` — Social auth endpoints (see [social-auth-app-django docs](https://python-social-auth.readthedocs.io/en/latest/configuration/django.html#urls))

**Providers:**
- `google-oauth2`
- `facebook`
- `github`
- `twitter`
- `linkedin-oauth2`

Example login URL: `/auth/login/google-oauth2/`

See the [official docs](https://python-social-auth.readthedocs.io/en/latest/backends/index.html) for provider-specific setup and callback URLs.

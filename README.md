# FastAPI Auth Backend

A simple authentication backend built with FastAPI, SQLAlchemy, and JWT-based access tokens. The project supports user registration, login, and protected user profile access via bearer tokens.

## Features

- User registration with email, name, and password
- Secure password hashing using bcrypt via PassLib
- Login endpoint issuing JWT bearer tokens
- Protected endpoint to return the current authenticated user
- SQLite database storage with SQLAlchemy ORM
- Environment-based configuration with `python-dotenv`

## Architecture

- `main.py` – Application entry point and router registration
- `config/config.py` – Application settings and environment loading
- `database/connection.py` – SQLAlchemy engine and base model setup
- `database/session.py` – SQLAlchemy session factory
- `models/user.py` – User ORM model definition
- `schemas/auth.py` – Request and response Pydantic schemas
- `routes/auth.py` – Authentication endpoints (`register`, `login`)
- `routes/user.py` – Protected user endpoint (`/api/users/me`)
- `services/auth_service.py` – Registration and login business logic
- `dependencies/auth_dependency.py` – DB session and current-user dependency
- `utils/jwt_token.py` – JWT token creation and verification
- `utils/security.py` – Password hashing and verification utilities

## Requirements

- Python 3.11+ (recommended)
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- python-jose
- passlib
- bcrypt

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Setup

1. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate
```

2. Install requirements:

```bash
pip install -r requirements.txt
```

3. (Optional) Add environment variables in a `.env` file:

```text
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///./data/users.db
TOKEN_EXPIRY_TIME_MINUTES=30
ALGORITHM=HS256
```

4. Initialize the database and run the app:

```bash
python main.py
```

The application will start on `http://0.0.0.0:8000`.

## API Endpoints

### Register

- `POST /api/auth/register`
- Request body:
  - `name` (string)
  - `email` (email)
  - `password` (string)

### Login

- `POST /api/auth/login`
- Request body:
  - `email` (email)
  - `password` (string)
  - `role` (`user` or `admin`)
- Response:
  - `access_token`
  - `token_type` (`bearer`)
  - `expires_in` (seconds)

### Get current user

- `GET /api/users/me`
- Requires `Authorization: Bearer <token>` header
- Returns the authenticated user profile

## Authentication

- JWTs are created using `python-jose`
- Tokens expire after `token_expiry_time_minutes` from configuration
- Protected endpoints validate bearer tokens using OAuth2 password bearer

## Notes

- The default database is SQLite at `./data/users.db`
- The app uses `settings.database_url` and loads `.env` variables if present
- `main.py` calls `init_db()` only when run as a script, creating tables automatically

## Development

- Use `uvicorn main:app --reload` for local development
- Keep secrets out of Git by using `.env` and `.gitignore`
- Add more protected routes by reusing `get_current_user` dependency

# 🎬 Cinema Backend API

**Cinema Backend API** is a modern backend for an online cinema, implemented with **FastAPI**.

The project provides a complete set of features for managing movie catalog, shopping cart, orders, payments, and user administration.

## 🚀 Key Features

- Secure authentication and authorization via **JWT**
- Role-based access control (**USER** / **MODERATOR** / **ADMIN**)
- Movie catalog management (titles, genres, age ratings)
- Complete shopping cart and order lifecycle
- Payment system integration (Stripe and others)
- Webhook processing (live + mock mode)
- Email notifications
- Automatic API documentation generation (OpenAPI/Swagger)
- Docker and Docker Compose support
- Automated tests + coverage report

## 📦 Technology Stack

| Component              | Technology                          |
|------------------------|-------------------------------------|
| Web framework          | FastAPI                             |
| ORM (async)            | SQLAlchemy 2.0+                     |
| Database (prod)        | PostgreSQL                          |
| Database (tests)       | SQLite                              |
| Payment system         | Stripe (or similar)                 |
| Containerization       | Docker + Docker Compose             |
| Dependency management  | Poetry                              |
| Testing                | pytest + pytest-asyncio             |
| Migrations             | Alembic                             |

## 🏗️ Project Structure

## 📡 Quick Start (Local Development)

1. Clone the repository

```bash
git clone https://github.com/Vasyl-Ch/Cinema-Backend-API.git
cd Cinema-Backend-API
git checkout developing
```

2. Create and configure .env
```bash
cp .env.sample .env
```

Make sure to fill in:

DATABASE_URL=postgresql://user:password@localhost:5432/cinema

SECRET_KEY=your-very-long-random-secret-key

STRIPE_API_KEY=sk_test_...

EMAIL_HOST=smtp.gmail.com

EMAIL_PORT=587

EMAIL_USER=your@gmail.com

EMAIL_PASSWORD=your-app-password


3. Start PostgreSQL and apply migrations
# create database (if not yet created)
createdb cinema

# apply migrations
alembic upgrade head

4. Install dependencies and run
```bash
poetry install
poetry shell
```
# start with auto-reload
uvicorn app.main:app --reload

Done! API is available at:
→ http://localhost:8000
→ Documentation: http://localhost:8000/docs

🧪 Testing

# regular test run
```bash
pytest
```
# with coverage
```bash
pytest --cov=app
```
🐳 Running via Docker Compose
# first run / rebuild
```bash
docker compose up --build
```
# stop
```bash
docker compose down
```

🔐 Authentication

Register user /auth/register
Get token /auth/login
Use header:

Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

📘 API Documentation

Swagger UI → http://localhost:8000/docs
ReDoc      → http://localhost:8000/redoc

💡 Useful Development Commands
```bash
# new migration
alembic revision --autogenerate -m "added payment status field"

# apply migrations
alembic upgrade head

# rollback last migration
alembic downgrade -1
```

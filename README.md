🎬 Online Cinema API
Online Cinema API is a backend solution built with FastAPI, designed to handle the complete workflow of an online cinema —
from exploring the movie catalog to managing orders, processing payments, and handling webhooks.

It is structured as a production-grade backend service, featuring authentication, role-based permissions, automated testing, documentation, and modern DevOps integration.

🔑 Core Features
Secure authentication and authorization using JWT

Role-based access control (USER / MODERATOR / ADMIN)

Movie catalog management (titles, genres, certifications)

Shopping cart functionality

Full order lifecycle management

Payment and refund support via Stripe

Stripe webhook handling (real + mock modes)

Email notifications

Comprehensive test coverage

Dependency management with Poetry

Containerization with Docker & Docker Compose

CI/CD pipelines powered by GitHub Actions

Complete API documentation with Swagger / OpenAPI 3.0

🏗️ Architecture Overview
FastAPI — REST API framework

SQLAlchemy (async) — ORM layer

PostgreSQL — production database

SQLite — lightweight test database

Stripe — payment gateway integration

Docker & Docker Compose — containerized deployment

Poetry — dependency/environment management

Pytest — automated testing framework

GitHub Actions — CI/CD automation

👥 User Roles
Role	Permissions
USER	Browse catalog, manage cart, place orders
MODERATOR	Manage movies and payment operations
ADMIN	Full system access, including user and role management
📖 API Documentation
The API is fully documented with OpenAPI 3.0 (Swagger).

Each endpoint includes:

concise summary and detailed description

request/response schemas

query and path parameters

expected HTTP responses

role-based access restrictions

Documentation Access Control
Swagger UI can be restricted to authenticated users via FastAPI configuration or middleware.

🧪 Testing & Coverage
Tools
pytest

pytest-asyncio

httpx.AsyncClient

coverage

Modules Covered
Module	Functionality Tested
Auth	registration, login, password reset/change
Movies	CRUD, filtering, role restrictions
Certifications	creation (ADMIN only)
Cart	add / remove / clear
Orders	create, cancel, list
Payments	create, refund, mock success
Webhooks	mock Stripe webhook
Users	admin-only user listing
✅ Positive and negative scenarios
✅ Role/permission enforcement
✅ Tests isolated from production database

🐳 Docker & Compose Setup
Supported Services
FastAPI

PostgreSQL

Redis

Celery

MinIO

▶️ Quick Start
bash
docker-compose up --build
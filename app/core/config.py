import os
from typing import Literal
from pydantic_settings import BaseSettings
from pydantic import field_validator, ConfigDict


class Settings(BaseSettings):
    """Application settings with validation"""

    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )

    # Database
    DATABASE_URL: str

    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # Stripe
    STRIPE_API_KEY: str
    STRIPE_WEBHOOK_SECRET: str | None = None

    # Mock Mode
    MOCK_MODE: bool = False
    MOCK_WEBHOOK: bool = False

    # CORS
    ALLOWED_ORIGINS: str

    # Email
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int = 587
    MAIL_SERVER: str = "smtp.gmail.com"
    MAIL_FROM_NAME: str = "Online Cinema"

    # Application
    ENVIRONMENT: Literal["development", "staging", "production"] = "development"
    LOG_LEVEL: str = "INFO"

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    @field_validator("SECRET_KEY")
    @classmethod
    def validate_secret_key(cls, v):
        if not v or v == "change-me" or len(v) < 32:
            raise ValueError(
                "SECRET_KEY must be at least 32 characters. "
                "Generate with: openssl rand -hex 32"
            )
        return v

    @field_validator("DATABASE_URL")
    @classmethod
    def validate_database_url(cls, v):
        if not v:
            raise ValueError("DATABASE_URL is required")
        if "sqlite" in v.lower() and os.getenv("ENVIRONMENT") == "production":
            raise ValueError("SQLite not allowed in production")
        return v

    @field_validator("ALLOWED_ORIGINS")
    @classmethod
    def validate_cors(cls, v):
        if not v or v == "*":
            raise ValueError("ALLOWED_ORIGINS must be explicitly set (no wildcards)")
        return v

    def is_production(self) -> bool:
        return self.ENVIRONMENT == "production"


settings = Settings()

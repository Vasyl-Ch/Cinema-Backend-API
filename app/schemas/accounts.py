from pydantic import BaseModel, EmailStr, Field, field_validator, ConfigDict
from datetime import datetime
from enum import Enum
from typing import Optional

from app.validators import validate_password_strength


class UserGroupEnum(str, Enum):
    USER = "USER"
    MODERATOR = "MODERATOR"
    ADMIN = "ADMIN"


class GenderEnum(str, Enum):
    MAN = "MAN"
    WOMAN = "WOMAN"


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(min_length=8)

    @field_validator("password")
    def strong_password(cls, v):
        return validate_password_strength(v)


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    avatar: Optional[str] = None
    gender: Optional[GenderEnum] = None
    date_of_birth: Optional[datetime] = None
    info: Optional[str] = None


class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    group: UserGroupEnum

    model_config = ConfigDict(from_attributes=True)

    # SQLAlchemy Enum → str
    @field_validator("group", mode="before")
    def convert_group(cls, value):
        if hasattr(value, "name"):
            return value.name
        return value


class UserLoginResponseSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class PasswordResetRequest(BaseModel):
    email: EmailStr


class PasswordReset(BaseModel):
    token: str
    new_password: str = Field(min_length=8)

    @field_validator("new_password")
    def strong_password(cls, v):
        return validate_password_strength(v)


class PasswordChange(BaseModel):
    old_password: str
    new_password: str = Field(min_length=8)

    @field_validator("new_password")
    def strong_password(cls, v):
        return validate_password_strength(v)


class ChangeUserRole(BaseModel):
    user_id: int
    new_role: UserGroupEnum


class ActivationTokenBase(BaseModel):
    token: str
    expires_at: datetime


class ActivationToken(ActivationTokenBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)


class RefreshTokenBase(BaseModel):
    token: str
    expires_at: datetime


class RefreshToken(RefreshTokenBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)

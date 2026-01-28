import os


os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///:memory:"
os.environ["MOCK_MODE"] = "True"


import pytest
import bcrypt
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
)
from sqlalchemy.orm import sessionmaker

from app.main import app as fastapi_app
from app.db.base import Base
from app.db.session import get_db
from app.models.accounts import User, UserGroup, UserGroupEnum
from app.utils.auth import create_access_token


engine_test = create_async_engine(
    "sqlite+aiosqlite:///:memory:",
    future=True,
)


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
async def db_connection():
    async with engine_test.connect() as connection:
        transaction = await connection.begin()
        try:
            yield connection
        finally:
            await transaction.rollback()


@pytest.fixture
async def db_session(db_connection):
    async_session = sessionmaker(
        bind=db_connection,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with async_session() as session:
        yield session


@pytest.fixture(autouse=True)
def override_get_db(db_session):
    async def _override():
        yield db_session

    fastapi_app.dependency_overrides[get_db] = _override


@pytest.fixture
async def client():
    transport = ASGITransport(app=fastapi_app)
    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as ac:
        yield ac


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


@pytest.fixture(autouse=True)
async def create_groups(db_session):
    for role in UserGroupEnum:
        exists = await db_session.execute(
            UserGroup.__table__.select().where(UserGroup.name == role)
        )
        if not exists.first():
            db_session.add(UserGroup(name=role))
    await db_session.commit()


@pytest.fixture
async def create_user(db_session, create_groups):

    async def _create(email: str, password: str, role: UserGroupEnum):
        result = await db_session.execute(
            User.__table__.select().where(User.email == email)
        )
        existing = result.first()
        if existing:
            return existing

        group = await db_session.execute(
            UserGroup.__table__.select().where(UserGroup.name == role)
        )
        group = group.first()
        if not group:
            raise RuntimeError("UserGroup not found")

        user = User(
            email=email,
            hashed_password=hash_password(password),
            is_active=True,
            group_id=group.id,
        )
        db_session.add(user)
        await db_session.commit()
        await db_session.refresh(user)
        return user

    return _create


@pytest.fixture
async def get_token():
    async def _token(user: User) -> str:
        return await create_access_token({"sub": user.email})
    return _token


@pytest.fixture
async def admin_user(create_user):
    return await create_user(
        "admin@test.com",
        "Admin123!",
        UserGroupEnum.ADMIN,
    )


@pytest.fixture
async def basic_user(create_user):
    return await create_user(
        "user@test.com",
        "User123!",
        UserGroupEnum.USER,
    )


@pytest.fixture
async def admin_token(admin_user, get_token):
    return await get_token(admin_user)


@pytest.fixture
async def user_token(basic_user, get_token):
    return await get_token(basic_user)

import pytest
from .factories import UserFactory

@pytest.fixture
def user_factory():
    return UserFactory

@pytest.fixture
def base_user(db, user_factory):
    user = user_factory.create(
        username="testuser",
        email="test@example.com",
        first_name="Test",
        last_name="User",
        password="testpass123",
        user_type="student"
    )
    return user

@pytest.fixture
def super_user(db, user_factory):
    user = user_factory.create(
        username="superuser",
        email="admin@example.com",
        first_name="Super",
        last_name="User",
        password="admin123",
        is_staff=True,
        is_superuser=True,
        user_type="instructor"
    )
    return user

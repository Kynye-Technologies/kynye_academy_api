import pytest
from apps.accounts.models import User


def test_user_str(base_user):
    """Test the custom user model string representation"""
    assert str(base_user) == base_user.username


def test_user_short_name(base_user):
    """Test that the user models get_short_name method works"""
    assert base_user.get_short_name() == base_user.username


def test_user_full_name(base_user):
    """Test that the user models get_full_name method works"""
    expected_full_name = f"{base_user.first_name} {base_user.last_name}"
    assert base_user.get_full_name == expected_full_name


@pytest.mark.django_db
class TestUserModelDB:
    def test_user_email_is_normalized(self, user_factory):
        """Test that a new users email is normalized"""
        email = "TEST.USER@EXAMPLE.COM"
        user = user_factory.create(email=email)
        assert user.email == email.lower()

        # Test email is normalized during update
        user.email = "NEW.TEST@EXAMPLE.COM"
        user.save()
        assert user.email == "new.test@example.com"

    def test_superuser_email_is_normalized(self, user_factory):
        """Test that an admin users email is normalized"""
        email = "ADMIN@EXAMPLE.COM"
        user = user_factory.create(email=email, is_superuser=True, is_staff=True)
        assert user.email == email.lower()

    def test_superuser_must_have_is_staff(self, user_factory):
        """Test that a superuser must have is_staff=True"""
        with pytest.raises(ValueError) as exc:
            user_factory.create(
                email="admin@example.com",
                password="admin123",
                is_superuser=True,
                is_staff=False
            )
        assert str(exc.value) == "Superusers must have is_staff=True"

    def test_superuser_must_have_is_superuser(self, user_factory):
        """Test that a superuser must have is_superuser=True"""
        with pytest.raises(ValueError) as exc:
            user_factory.create(
                email="admin@example.com",
                password="admin123",
                is_superuser=False,
                is_staff=True
            )
        assert str(exc.value) == "Superusers must have is_superuser=True"

    def test_create_user_with_no_email(self, user_factory):
        """Test creating a user without an email raises error"""
        with pytest.raises(ValueError) as exc:
            user_factory.create(email=None)
        assert str(exc.value) == "Base User Account: An email address is required"

    def test_create_user_with_no_username(self, user_factory):
        """Test creating a user without a username raises error"""
        with pytest.raises(ValueError) as exc:
            user_factory.create(username=None)
        assert str(exc.value) == "Users must submit a username"

    def test_create_user_with_no_firstname(self, user_factory):
        """Test creating a user without a firstname raises error"""
        with pytest.raises(ValueError) as exc:
            user_factory.create(first_name=None)
        assert str(exc.value) == "Users must submit a first name"

    def test_create_user_with_no_lastname(self, user_factory):
        """Test creating a user without a lastname raises error"""
        with pytest.raises(ValueError) as exc:
            user_factory.create(last_name=None)
        assert str(exc.value) == "Users must submit a last name"

    def test_create_superuser_with_no_email(self, user_factory):
        """Test creating a superuser without an email raises error"""
        with pytest.raises(ValueError) as exc:
            user_factory.create(
                email=None,
                is_superuser=True,
                is_staff=True
            )
        assert str(exc.value) == "Admin Account: An email address is required"

    def test_create_superuser_with_no_password(self, user_factory):
        """Test creating a superuser without a password raises error"""
        with pytest.raises(ValueError) as exc:
            user_factory.create(
                email="admin@example.com",
                password=None,
                is_superuser=True,
                is_staff=True
            )
        assert str(exc.value) == "Superusers must have a password"

    def test_user_email_validator(self, user_factory):
        """Test that an invalid email format raises error"""
        with pytest.raises(ValueError) as exc:
            user_factory.create(email="invalid-email")
        assert str(exc.value) == "You must provide a valid email address"

    def test_user_type_choices(self, user_factory):
        """Test that user_type must be either 'student' or 'instructor'"""
        user = user_factory.create(user_type="student")
        assert user.user_type in ["student", "instructor"]

        user = user_factory.create(user_type="instructor")
        assert user.user_type in ["student", "instructor"]

from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must provide a valid email address"))

    def create_user(self, username=None, first_name=None, last_name=None, email=None, password=None, user_type='student', **extra_fields):
        if email is None:
            raise ValueError(_("Base User Account: An email address is required"))
        email = self.normalize_email(email).lower()
        self.email_validator(email)

        # If called from normal signup/tests, require all fields
        if username is None:
            raise ValueError(_("Users must submit a username"))
        if first_name is None:
            raise ValueError(_("Users must submit a first name"))
        if last_name is None:
            raise ValueError(_("Users must submit a last name"))
        if user_type is None:
            raise ValueError(_("Users must submit a user type"))

        # If called from social-auth, auto-generate missing fields (they will be empty string, not None)
        if not username:
            username = email.split('@')[0]
        if not first_name:
            first_name = ''
        if not last_name:
            last_name = ''
        if not user_type:
            user_type = 'student'
        if not password:
            password = self.make_random_password()

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            user_type=user_type,
            **extra_fields
        )
        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, email, password, user_type='instructor', **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superusers must have is_staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superusers must have is_superuser=True"))
        if not password:
            raise ValueError(_("Superusers must have a password"))
        if not email:
            raise ValueError(_("Admin Account: An email address is required"))
            
        email = self.normalize_email(email).lower()
        self.email_validator(email)

        user = self.create_user(
            username, first_name, last_name, email, password, user_type, **extra_fields
        )
        user.save(using=self._db)
        return user

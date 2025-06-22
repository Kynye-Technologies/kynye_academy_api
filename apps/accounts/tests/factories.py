import factory
from django.conf import settings
from apps.accounts.models import User  # Direct import instead of get_user_model
from faker import Faker

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda _: fake.user_name())
    email = factory.LazyAttribute(lambda _: fake.email())
    first_name = factory.LazyAttribute(lambda _: fake.first_name())
    last_name = factory.LazyAttribute(lambda _: fake.last_name())
    password = factory.LazyAttribute(lambda _: fake.password())
    is_active = True
    is_staff = False
    user_type = 'student'

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override the default _create to handle the password hashing."""
        manager = cls._get_manager(model_class)
        if 'is_superuser' in kwargs:
            return manager.create_superuser(*args, **kwargs)
        return manager.create_user(*args, **kwargs)

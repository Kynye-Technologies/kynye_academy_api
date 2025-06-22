import factory
from django.contrib.auth import get_user_model
from apps.profiles.models import InstructorProfile, StudentProfile

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda o: f'{o.username}@example.com')
    first_name = 'John'
    last_name = 'Doe'
    user_type = 'student'
    is_active = True

class InstructorProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = InstructorProfile
        django_get_or_create = ('user',)
    user = factory.SubFactory(UserFactory, user_type='instructor')
    bio = factory.Faker('paragraph')
    main_expertise = 'Web Development'
    category = 'Fullstack'
    specialization = 'MERN Stack'
    years_of_experience = 3
    rating = 4.5

class StudentProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StudentProfile
        django_get_or_create = ('user',)
    user = factory.SubFactory(UserFactory, user_type='student')
    bio = factory.Faker('paragraph')

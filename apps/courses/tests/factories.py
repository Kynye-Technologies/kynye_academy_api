# Factories for courses app

import factory
from apps.courses import models
from apps.profiles.tests.factories import UserFactory

class MainExpertiseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.MainExpertise
    name = factory.Sequence(lambda n: f"MainExpertise{n}")

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category
    name = factory.Sequence(lambda n: f"Category{n}")
    main_expertise = factory.SubFactory(MainExpertiseFactory)

class SpecializationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Specialization
    name = factory.Sequence(lambda n: f"Specialization{n}")
    category = factory.SubFactory(CategoryFactory)

class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Course
    title = factory.Sequence(lambda n: f"Course{n}")
    description = factory.Faker('paragraph')
    instructor = factory.SubFactory(UserFactory, user_type='instructor')
    specialization = factory.SubFactory(SpecializationFactory)

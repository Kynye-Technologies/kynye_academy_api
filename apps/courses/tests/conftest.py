# Pytest fixtures for courses app

import pytest
from apps.courses.tests.factories import (
    MainExpertiseFactory, CategoryFactory, SpecializationFactory, CourseFactory
)
from apps.profiles.tests.factories import UserFactory

@pytest.fixture
def main_expertise():
    return MainExpertiseFactory(name='Web Development')

@pytest.fixture
def category(main_expertise):
    return CategoryFactory(name='Fullstack', main_expertise=main_expertise)

@pytest.fixture
def specialization(category):
    return SpecializationFactory(name='MERN Stack', category=category)

@pytest.fixture
def instructor_user():
    return UserFactory(user_type='instructor')

@pytest.fixture
def student_user():
    return UserFactory(user_type='student')

@pytest.fixture
def course_factory():
    return CourseFactory

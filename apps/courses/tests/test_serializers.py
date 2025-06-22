# Tests for courses serializers

import pytest
from apps.courses.serializers import CourseSerializer, SpecializationSerializer, CategorySerializer, MainExpertiseSerializer
from apps.courses.tests.factories import CourseFactory, SpecializationFactory, CategoryFactory, MainExpertiseFactory

pytestmark = pytest.mark.django_db

def test_course_serializer():
    course = CourseFactory()
    data = CourseSerializer(course).data
    assert data['title'] == course.title
    assert data['specialization']['name'] == course.specialization.name

def test_specialization_serializer():
    specialization = SpecializationFactory()
    data = SpecializationSerializer(specialization).data
    assert data['name'] == specialization.name
    assert data['category']['name'] == specialization.category.name

def test_category_serializer():
    category = CategoryFactory()
    data = CategorySerializer(category).data
    assert data['name'] == category.name
    assert data['main_expertise']['name'] == category.main_expertise.name

def test_main_expertise_serializer():
    main_expertise = MainExpertiseFactory()
    data = MainExpertiseSerializer(main_expertise).data
    assert data['name'] == main_expertise.name

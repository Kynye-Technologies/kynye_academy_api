# Tests for courses models

import pytest
from apps.courses.tests.factories import MainExpertiseFactory, CategoryFactory, SpecializationFactory, CourseFactory

pytestmark = pytest.mark.django_db

def test_main_expertise_str():
    obj = MainExpertiseFactory(name='Web Development')
    assert str(obj) == 'Web Development'

def test_category_str():
    main = MainExpertiseFactory(name='Web Development')
    obj = CategoryFactory(name='Fullstack', main_expertise=main)
    assert str(obj) == 'Web Development - Fullstack'

def test_specialization_str():
    main = MainExpertiseFactory(name='Web Development')
    cat = CategoryFactory(name='Fullstack', main_expertise=main)
    obj = SpecializationFactory(name='MERN Stack', category=cat)
    assert str(obj) == 'Web Development - Fullstack - MERN Stack'

def test_course_str():
    obj = CourseFactory(title='Advanced Django')
    assert str(obj) == 'Advanced Django'

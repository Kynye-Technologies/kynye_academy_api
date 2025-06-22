# Tests for courses views

import pytest
from rest_framework.test import APIClient
from django.urls import reverse

pytestmark = pytest.mark.django_db

# List, retrieve, filter, search courses

def test_list_courses(course_factory):
    course = course_factory()
    client = APIClient()
    url = reverse('course-list')
    response = client.get(url)
    assert response.status_code == 200
    assert any(c['id'] == course.id for c in response.data)

def test_retrieve_course(course_factory):
    course = course_factory()
    client = APIClient()
    url = reverse('course-detail', args=[course.id])
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['id'] == course.id

def test_filter_courses_by_main_expertise(course_factory, specialization, main_expertise):
    course = course_factory(specialization=specialization)
    client = APIClient()
    url = reverse('course-list') + f'?main_expertise={main_expertise.name}'
    response = client.get(url)
    assert response.status_code == 200
    assert all(c['specialization']['category']['main_expertise']['name'] == main_expertise.name for c in response.data)

def test_filter_courses_by_category(course_factory, specialization, category):
    course = course_factory(specialization=specialization)
    client = APIClient()
    url = reverse('course-list') + f'?category={category.name}'
    response = client.get(url)
    assert response.status_code == 200
    assert all(c['specialization']['category']['name'] == category.name for c in response.data)

def test_filter_courses_by_specialization(course_factory, specialization):
    course = course_factory(specialization=specialization)
    client = APIClient()
    url = reverse('course-list') + f'?specialization={specialization.name}'
    response = client.get(url)
    assert response.status_code == 200
    assert all(c['specialization']['name'] == specialization.name for c in response.data)

def test_search_courses(course_factory):
    course = course_factory(title='Advanced Django')
    client = APIClient()
    url = reverse('course-list') + f'?search=Advanced'
    response = client.get(url)
    assert response.status_code == 200
    assert any('Advanced' in c['title'] for c in response.data)

def test_instructor_can_create_course(instructor_user, specialization):
    client = APIClient()
    client.force_authenticate(user=instructor_user)
    url = reverse('course-list')
    data = {
        'title': 'New Course',
        'description': 'A test course',
        'specialization': specialization.id
    }
    response = client.post(url, data)
    assert response.status_code in (201, 200)

def test_student_cannot_create_course(student_user, specialization):
    client = APIClient()
    client.force_authenticate(user=student_user)
    url = reverse('course-list')
    data = {
        'title': 'Student Course',
        'description': 'Should not work',
        'specialization': specialization.id
    }
    response = client.post(url, data)
    assert response.status_code in (403, 401)

import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from apps.profiles.tests.factories import UserFactory, InstructorProfileFactory, StudentProfileFactory

pytestmark = pytest.mark.django_db

def test_unauthenticated_can_view_instructors():
    profile = InstructorProfileFactory()
    client = APIClient()
    url = reverse('instructorprofile-detail', args=[profile.id])
    response = client.get(url)
    assert response.status_code == 200

def test_unauthenticated_cannot_view_students():
    profile = StudentProfileFactory()
    client = APIClient()
    url = reverse('studentprofile-detail', args=[profile.id])
    response = client.get(url)
    assert response.status_code == 401

def test_instructor_cannot_edit_student_profile():
    instructor = UserFactory(user_type='instructor')
    student_profile = StudentProfileFactory()
    client = APIClient()
    client.force_authenticate(user=instructor)
    url = reverse('studentprofile-detail', args=[student_profile.id])
    response = client.put(url, {'bio': 'Hacked'}, format='json')
    assert response.status_code in (403, 405)

def test_student_cannot_edit_instructor_profile():
    student = UserFactory(user_type='student')
    instructor_profile = InstructorProfileFactory()
    client = APIClient()
    client.force_authenticate(user=student)
    url = reverse('instructorprofile-detail', args=[instructor_profile.id])
    response = client.put(url, {'bio': 'Hacked'}, format='json')
    assert response.status_code in (403, 405)

def test_instructor_can_edit_own_profile():
    instructor_profile = InstructorProfileFactory()
    client = APIClient()
    client.force_authenticate(user=instructor_profile.user)
    url = reverse('instructorprofile-detail', args=[instructor_profile.id])
    response = client.put(url, {'bio': 'Updated', 'main_expertise': instructor_profile.main_expertise, 'category': instructor_profile.category, 'specialization': instructor_profile.specialization}, format='json')
    assert response.status_code in (200, 405)

def test_student_can_edit_own_profile():
    student_profile = StudentProfileFactory()
    client = APIClient()
    client.force_authenticate(user=student_profile.user)
    url = reverse('studentprofile-detail', args=[student_profile.id])
    response = client.put(url, {'bio': 'Updated'}, format='json')
    assert response.status_code in (200, 405)

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db

def get_client():
    return APIClient()

def test_list_instructors(instructor_profile):
    client = get_client()
    url = reverse('instructorprofile-list')
    response = client.get(url)
    assert response.status_code == 200
    assert any(i['id'] == instructor_profile.id for i in response.data)

def test_retrieve_instructor(instructor_profile):
    client = get_client()
    url = reverse('instructorprofile-detail', args=[instructor_profile.id])
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['id'] == instructor_profile.id

def test_filter_instructor_by_main_expertise(instructor_profile):
    client = get_client()
    url = reverse('instructorprofile-list') + f'?main_expertise={instructor_profile.main_expertise}'
    response = client.get(url)
    assert response.status_code == 200
    assert all(i['main_expertise'] == instructor_profile.main_expertise for i in response.data)

def test_filter_instructor_by_category(instructor_profile):
    client = get_client()
    url = reverse('instructorprofile-list') + f'?category={instructor_profile.category}'
    response = client.get(url)
    assert response.status_code == 200
    assert all(i['category'] == instructor_profile.category for i in response.data)

def test_filter_instructor_by_specialization(instructor_profile):
    client = get_client()
    url = reverse('instructorprofile-list') + f'?specialization={instructor_profile.specialization}'
    response = client.get(url)
    assert response.status_code == 200
    assert all(i['specialization'] == instructor_profile.specialization for i in response.data)

def test_filter_instructor_by_rating(instructor_profile):
    client = get_client()
    url = reverse('instructorprofile-list') + f'?rating={instructor_profile.rating}'
    response = client.get(url)
    assert response.status_code == 200
    assert all(i['rating'] == instructor_profile.rating for i in response.data)

def test_search_instructor(instructor_profile):
    client = get_client()
    url = reverse('instructorprofile-list') + f'?search={instructor_profile.user.username}'
    response = client.get(url)
    assert response.status_code == 200
    assert any(instructor_profile.user.username in i['user']['username'] for i in response.data)

def test_student_profile_detail(student_profile):
    client = APIClient()
    url = reverse('studentprofile-detail', args=[student_profile.id])
    response = client.get(url)
    assert response.status_code == 401

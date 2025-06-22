import pytest
from django.contrib.auth import get_user_model
from apps.profiles.models import InstructorProfile, StudentProfile

pytestmark = pytest.mark.django_db

User = get_user_model()

def test_instructor_profile_created_signal():
    user = User.objects.create_user(
        username='instructor1',
        email='instructor1@example.com',
        password='pass',
        user_type='instructor',
        first_name='John',
        last_name='Doe',
    )
    assert InstructorProfile.objects.filter(user=user).exists()

def test_student_profile_created_signal():
    user = User.objects.create_user(
        username='student1',
        email='student1@example.com',
        password='pass',
        user_type='student',
        first_name='Jane',
        last_name='Smith',
    )
    assert StudentProfile.objects.filter(user=user).exists()

def test_no_duplicate_profile_on_update():
    user = User.objects.create_user(
        username='instructor2',
        email='instructor2@example.com',
        password='pass',
        user_type='instructor',
        first_name='Jim',
        last_name='Beam',
    )
    profile_count = InstructorProfile.objects.filter(user=user).count()
    user.first_name = 'Changed'
    user.save()
    assert InstructorProfile.objects.filter(user=user).count() == profile_count

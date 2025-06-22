import pytest
from apps.profiles.models import InstructorProfile, StudentProfile
from apps.profiles.tests.factories import InstructorProfileFactory, StudentProfileFactory

pytestmark = pytest.mark.django_db

def test_instructor_profile_str():
    profile = InstructorProfileFactory()
    assert str(profile) == f"InstructorProfile({profile.user.username})"

def test_student_profile_str():
    profile = StudentProfileFactory()
    assert str(profile) == f"StudentProfile({profile.user.username})"

def test_instructor_profile_fields():
    profile = InstructorProfileFactory()
    assert profile.main_expertise
    assert profile.category
    assert profile.specialization
    assert profile.user
    assert profile.rating >= 0

def test_student_profile_fields():
    profile = StudentProfileFactory()
    assert profile.user
    assert hasattr(profile, 'bio')
    assert hasattr(profile, 'profile_picture')
    assert hasattr(profile, 'phone_number')

import pytest
from apps.profiles.serializers import InstructorProfileSerializer, StudentProfileSerializer
from apps.profiles.tests.factories import InstructorProfileFactory, StudentProfileFactory

pytestmark = pytest.mark.django_db

def test_instructor_profile_serializer():
    profile = InstructorProfileFactory()
    data = InstructorProfileSerializer(profile).data
    assert data['user']['username'] == profile.user.username
    assert data['main_expertise'] == profile.main_expertise
    assert data['category'] == profile.category
    assert data['specialization'] == profile.specialization

def test_student_profile_serializer():
    profile = StudentProfileFactory()
    data = StudentProfileSerializer(profile).data
    assert data['user']['username'] == profile.user.username
    assert 'bio' in data
    assert 'profile_picture' in data

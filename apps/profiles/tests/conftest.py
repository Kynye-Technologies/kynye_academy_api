import pytest
from apps.profiles.tests.factories import InstructorProfileFactory, StudentProfileFactory

@pytest.fixture
def instructor_profile():
    return InstructorProfileFactory()

@pytest.fixture
def student_profile():
    return StudentProfileFactory()

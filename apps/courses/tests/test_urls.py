# Tests for courses urls

from django.urls import reverse, resolve
from apps.courses.views import CourseList, CourseDetail

def test_course_list_url():
    url = reverse('course-list')
    assert resolve(url).func.view_class == CourseList

def test_course_detail_url():
    url = reverse('course-detail', args=[1])
    assert resolve(url).func.view_class == CourseDetail

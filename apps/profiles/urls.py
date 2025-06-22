from django.urls import path
from .views import (
    InstructorProfileList, InstructorProfileDetail, StudentProfileDetail
)

urlpatterns = [
    path('instructors/', InstructorProfileList.as_view(), name='instructorprofile-list'),
    path('instructors/<int:pk>/', InstructorProfileDetail.as_view(), name='instructorprofile-detail'),
    path('students/<int:pk>/', StudentProfileDetail.as_view(), name='studentprofile-detail'),
]

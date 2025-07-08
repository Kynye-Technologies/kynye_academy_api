from django.urls import path
from .views import FileUploadView, TaskStatusView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='analytics-file-upload'),
    path('task-status/<str:task_id>/', TaskStatusView.as_view(), name='analytics-task-status'),
]

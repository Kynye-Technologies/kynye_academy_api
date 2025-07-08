from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.core.files.storage import default_storage
from django.conf import settings
import os
from .tasks import process_uploaded_file
from .serializers import FileUploadSerializer
from celery.result import AsyncResult
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

class FileUploadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Upload a CSV file for background processing.",
        request_body=FileUploadSerializer,
        responses={202: openapi.Response('Accepted', schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'task_id': openapi.Schema(type=openapi.TYPE_STRING),
                'message': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ))}
    )
    def post(self, request):
        serializer = FileUploadSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        uploaded_file = serializer.validated_data['file']
        file_path = default_storage.save(f"uploads/{uploaded_file.name}", uploaded_file)
        abs_path = os.path.join(settings.MEDIA_ROOT, file_path)
        # Trigger background processing
        task = process_uploaded_file.delay(abs_path)
        return Response({'task_id': task.id, 'message': 'File uploaded and processing started.'}, status=status.HTTP_202_ACCEPTED)

class TaskStatusView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get the status and result of a background task.",
        manual_parameters=[
            openapi.Parameter('task_id', openapi.IN_PATH, description="Celery Task ID", type=openapi.TYPE_STRING)
        ],
        responses={200: openapi.Response('Task Status', schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'task_id': openapi.Schema(type=openapi.TYPE_STRING),
                'status': openapi.Schema(type=openapi.TYPE_STRING),
                'result': openapi.Schema(type=openapi.TYPE_OBJECT),
            }
        ))}
    )
    def get(self, request, task_id):
        result = AsyncResult(task_id)
        response = {
            'task_id': task_id,
            'status': result.status,
            'result': result.result if result.successful() else None,
        }
        return Response(response)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Course
from .serializers import CourseSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Q

class CourseList(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        queryset = Course.objects.all()
        main_expertise = request.GET.get('main_expertise')
        category = request.GET.get('category')
        specialization = request.GET.get('specialization')
        search = request.GET.get('search')
        if main_expertise:
            queryset = queryset.filter(specialization__category__main_expertise__name=main_expertise)
        if category:
            queryset = queryset.filter(specialization__category__name=category)
        if specialization:
            queryset = queryset.filter(specialization__name=specialization)
        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(description__icontains=search))
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_authenticated or request.user.user_type != 'instructor':
            return Response({'detail': 'Only instructors can create courses.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(instructor=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetail(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import InstructorProfile, StudentProfile
from .serializers import InstructorProfileSerializer, StudentProfileSerializer
from .permissions import IsInstructorOrReadOnly, IsStudentOrReadOnly, IsAuthenticatedOrInstructorListOnly
from django.shortcuts import get_object_or_404
from django.db.models import Q

class InstructorProfileList(APIView):
    permission_classes = [IsAuthenticatedOrInstructorListOnly]

    def get(self, request):
        queryset = InstructorProfile.objects.all()
        main_expertise = request.GET.get('main_expertise')
        category = request.GET.get('category')
        specialization = request.GET.get('specialization')
        rating = request.GET.get('rating')
        search = request.GET.get('search')
        if main_expertise:
            queryset = queryset.filter(main_expertise=main_expertise)
        if category:
            queryset = queryset.filter(category=category)
        if specialization:
            queryset = queryset.filter(specialization=specialization)
        if rating:
            queryset = queryset.filter(rating=rating)
        if search:
            queryset = queryset.filter(
                Q(user__username__icontains=search) |
                Q(user__first_name__icontains=search) |
                Q(user__last_name__icontains=search)
            )
        serializer = InstructorProfileSerializer(queryset, many=True)
        return Response(serializer.data)

class InstructorProfileDetail(APIView):
    permission_classes = [IsInstructorOrReadOnly | permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        profile = get_object_or_404(InstructorProfile, pk=pk)
        serializer = InstructorProfileSerializer(profile)
        return Response(serializer.data)

class StudentProfileDetail(APIView):
    permission_classes = [IsStudentOrReadOnly, permissions.IsAuthenticated]

    def get(self, request, pk):
        profile = get_object_or_404(StudentProfile, pk=pk)
        serializer = StudentProfileSerializer(profile)
        return Response(serializer.data)

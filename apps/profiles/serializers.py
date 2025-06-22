from rest_framework import serializers
from .models import InstructorProfile, StudentProfile
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'user_type')

class InstructorProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = InstructorProfile
        fields = [
            'id', 'user', 'bio', 'profile_picture',
            'main_expertise', 'category', 'specialization',
            'years_of_experience', 'social_links', 'phone_number', 'rating'
        ]

class StudentProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = StudentProfile
        fields = '__all__'

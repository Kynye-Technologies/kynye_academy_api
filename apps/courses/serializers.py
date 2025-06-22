from rest_framework import serializers
from .models import MainExpertise, Category, Specialization, Course
from django.contrib.auth import get_user_model

class MainExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainExpertise
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    main_expertise = MainExpertiseSerializer(read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'main_expertise']

class SpecializationSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Specialization
        fields = ['id', 'name', 'category']

class CourseSerializer(serializers.ModelSerializer):
    instructor = serializers.PrimaryKeyRelatedField(read_only=True)
    specialization = serializers.PrimaryKeyRelatedField(queryset=Specialization.objects.all())

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'instructor', 'specialization', 'created_at', 'updated_at']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['specialization'] = SpecializationSerializer(instance.specialization).data
        return rep

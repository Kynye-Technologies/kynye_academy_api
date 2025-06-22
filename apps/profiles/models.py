from django.db import models
from django.conf import settings

class InstructorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='instructor_profile')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='instructors/', blank=True, null=True)
    main_expertise = models.CharField(max_length=100, default='Web Development')  # e.g., Web Development, Data Science
    category = models.CharField(max_length=100, default='Fullstack')        # e.g., Fullstack, Backend, Frontend
    specialization = models.CharField(max_length=100, default='MERN Stack')  # e.g., MERN Stack, Django, React
    years_of_experience = models.PositiveIntegerField(blank=True, null=True)
    social_links = models.JSONField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True)
    rating = models.FloatField(default=0)
    
    def __str__(self):
        return f"InstructorProfile({self.user.username})"

class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='students/', blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return f"StudentProfile({self.user.username})"

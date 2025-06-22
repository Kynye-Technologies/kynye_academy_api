from django.db import models
from django.conf import settings

class MainExpertise(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    main_expertise = models.ForeignKey(MainExpertise, on_delete=models.CASCADE, related_name='categories')
    def __str__(self):
        return f"{self.main_expertise.name} - {self.name}"

class Specialization(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='specializations')
    def __str__(self):
        return f"{self.category.main_expertise.name} - {self.category.name} - {self.name}"

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses')
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

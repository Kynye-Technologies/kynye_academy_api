from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from apps.accounts.models import User
from .models import InstructorProfile, StudentProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'instructor':
            InstructorProfile.objects.create(
                user=instance,
                main_expertise='Web Development',
                category='Fullstack',
                specialization='MERN Stack',
            )
        elif instance.user_type == 'student':
            StudentProfile.objects.create(user=instance)

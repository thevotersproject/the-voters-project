from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AdminProfile


@receiver(post_save, sender=User)
def adminCreation(sender, instance, created, **kwargs):
    if created:
        AdminProfile.objects.create(user=instance)

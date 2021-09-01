from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class AdminProfile(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    bio = models.TextField(null=True)

    def __str__(self):
        return self.admin.username

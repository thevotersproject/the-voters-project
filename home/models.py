from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class AdminProfile(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    role = models.CharField(max_length=50)

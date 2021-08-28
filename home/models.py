from django.db import models


# Create your models here.
class Admin(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

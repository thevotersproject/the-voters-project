from django.db import models


# Create your models here.
class Admin(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

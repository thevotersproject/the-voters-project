from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserTable(models.Model):
    admin = models.ForeignKey(User, default=5, on_delete=models.CASCADE)
    userFirstname = models.CharField(max_length=100)
    userLastname = models.CharField(max_length=100)
    userImg = models.ImageField(upload_to='pics')
    userFingerprint = models.IntegerField(unique=True, null=False)

    def __str__(self):
        return self.userFirstname + ' ' + self.userLastname


class CandidateTable(models.Model):
    admin = models.ForeignKey(User, default=5, on_delete=models.CASCADE)
    candidateFirstname = models.CharField(max_length=100)
    candidateLastname = models.CharField(max_length=100)
    candidateDetails = models.TextField()
    candidateImg = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.candidateFirstname + ' ' + self.candidateLastname


class EventTable(models.Model):
    admin = models.ForeignKey(User, default=5, on_delete=models.CASCADE)
    eventName = models.CharField(max_length=100)
    eventDetails = models.TextField()
    eventPosition = models.CharField(max_length=100)
    eventStartDate = models.DateTimeField()
    eventEndDate = models.DateTimeField()

    def __str__(self):
        return self.eventName + '|' + str(self.eventStartDate.date()) + '|' + str(self.eventEndDate.date())

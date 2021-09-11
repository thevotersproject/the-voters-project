from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.


class VoterTable(models.Model):
    admin = models.ForeignKey(User, default=5, on_delete=models.CASCADE)
    voterFirstname = models.CharField(max_length=100)
    voterLastname = models.CharField(max_length=100)
    voterImg = models.ImageField(upload_to='pics')
    voterFingerprint = models.IntegerField(unique=True, null=False)

    def __str__(self):
        return self.voterFirstname + ' ' + self.voterLastname


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
    eventUUID = models.UUIDField(default=uuid.uuid4, editable=False)
    eventStartDate = models.DateTimeField()
    eventEndDate = models.DateTimeField()

    def __str__(self):
        return self.eventName + '|' + str(self.eventStartDate.date()) + '|' + str(self.eventEndDate.date())


class VoterEvent(models.Model):
    voter = models.ForeignKey(VoterTable, on_delete=models.CASCADE)
    event = models.ForeignKey(EventTable, on_delete=models.CASCADE)


class CandidateEvent(models.Model):
    candidate = models.ForeignKey(CandidateTable, on_delete=models.CASCADE)
    event = models.ForeignKey(EventTable, on_delete=models.CASCADE)

from django import forms
# from django.forms import ModelForm
from .models import *


class CandidateForm(forms.ModelForm):
    class Meta:
        model = CandidateTable
        fields = ('admin', 'candidateImg', 'candidateFirstname', 'candidateLastname', 'candidateDetails')

        labels = {
            'admin': 'Current Admin',
            'candidateImg': 'Select Image',
            'candidateFirstname': 'First Name',
            'candidateLastname': 'Last Name',
            'candidateDetails': 'Details',
        }
        widgets = {
            'admin': forms.Select(attrs={'class': 'form-control'}),
            'candidateImg': forms.FileInput(attrs={'class': 'form-control'}),
            'candidateFirstname': forms.TextInput(attrs={'class': 'form-control'}),
            'candidateLastname': forms.TextInput(attrs={'class': 'form-control'}),
            'candidateDetails': forms.Textarea(attrs={'class': 'form-control'}),
        }


class VoterForm(forms.ModelForm):
    class Meta:
        model = VoterTable
        fields = ('admin', 'voterImg', 'voterFirstname', 'voterLastname', 'voterFingerprint')

        labels = {
            'admin': 'Current Admin',
            'voterImg': 'Select Image',
            'voterFirstname': 'First Name',
            'voterLastname': 'Last Name',
            'voterFingerprint': 'Fingerprint',
        }

        widgets = {
            'admin': forms.Select(attrs={'class': 'form-control'}),
            'voterImg': forms.FileInput(attrs={'class': 'form-control'}),
            'voterFirstname': forms.TextInput(attrs={'class': 'form-control'}),
            'voterLastname': forms.TextInput(attrs={'class': 'form-control'}),
            'voterFingerprint': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = EventTable
        fields = ('admin', 'eventName', 'eventPosition', 'eventDetails', 'eventStartDate', 'eventEndDate')

        labels = {
            'admin': 'Current Admin',
            'eventName': 'Event Name',
            'eventPosition': 'Position',
            'eventDetails': 'Event Details',
            'eventStartDate': 'Start Date',
            'eventEndDate': 'End Date',
        }

        widgets = {
            'admin': forms.Select(attrs={'class': 'form-control'}),
            'eventName': forms.TextInput(attrs={'class': 'form-control'}),
            'eventPosition': forms.TextInput(attrs={'class': 'form-control'}),
            'eventDetails': forms.Textarea(attrs={'class': 'form-control'}),
            'eventStartDate': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'eventEndDate': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }

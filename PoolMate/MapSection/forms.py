from django import forms
from .models import Route

class CreateRideForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['origin', 'destination']

from django.forms import ModelForm

from django import forms

class AvailabilityForm(forms.Form):
    
    destination=forms.CharField(max_length=50, required=True)
    check_in= forms.DateTimeField(required=True,input_formats=["%Y-%m-%dT%H:%M"] )
    check_out= forms.DateTimeField(required=True,input_formats=["%Y-%m-%dT%H:%M"])

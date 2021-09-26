from django import forms
from . models import Location

class LocationModelForm(forms.ModelForm):
    class Meta:
        Model=Location
        fields=('destination',)
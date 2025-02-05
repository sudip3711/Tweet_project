from django import forms
from .models import Tweet

class TwwetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields =['text','image']
from django import forms

from .models import Link, Review

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('name', 'url',)
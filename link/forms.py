from django import forms

from .models import Link, Review

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('name', 'url',)
        widgets = {
            'name': forms.TextInput(attrs={'class':'w-full mt-2 py-4 px-6 bg-slate-100 border-slate-300'}),
            'url': forms.TextInput(attrs={'class':'w-full mt-2 py-4 px-6 bg-slate-100 border-slate-300'})
        }
from django import forms
from .models import Polozka

class PolozkaForm(forms.ModelForm):
    class Meta:
        model = Polozka
        fields = ['nazev', 'popis', 'hodnoceni', 'stav']
        widgets = {
            'nazev': forms.TextInput(attrs={'class': 'form-control'}),
            'popis': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'hodnoceni': forms.Select(attrs={'class': 'form-select'}),
            'stav': forms.Select(attrs={'class': 'form-select'}),
        }

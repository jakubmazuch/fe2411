from django import forms
from .models import Ukol


class UkolForm(forms.ModelForm):
    class Meta:
        model = Ukol
        fields = ['nazev', 'popis', 'termin', 'priorita']
        widgets = {
            'nazev': forms.TextInput(attrs={'class': 'form-control'}),
            'popis': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'termin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'priorita': forms.Select(attrs={'class': 'form-select'}),
        }

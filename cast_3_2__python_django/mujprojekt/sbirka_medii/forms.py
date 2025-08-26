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
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if self.errors.get(field_name):
                css_class = field.widget.attrs.get("class", "")
                field.widget.attrs["class"] = f"{css_class} is-invalid"
            
    

    def clean_popis(self):
        popis = self.cleaned_data.get("popis", "")
        if len(popis.strip()) < 10:
            raise forms.ValidationError("Popis musí mít alespoň 10 znaků.")
        return popis

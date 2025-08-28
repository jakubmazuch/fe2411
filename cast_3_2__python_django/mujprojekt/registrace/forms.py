from django import forms
from .models import Uzivatel


class RegistraceForm(forms.ModelForm):
    heslo1 = forms.CharField(
        label="Heslo",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Zadejte heslo",
        })
    )

    heslo2 = forms.CharField(
        label="Potvrzení hesla",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Zadejte heslo ještě jednou",
        })
    )

    class Meta:
        model = Uzivatel
        fields = ["jmeno", "prijmeni", "email"]
        labels = {
            "jmeno": "Jméno: ",
            "prijmeni": "Příjmení: ",
            "email": "E-mail: ",
        }
        widgets = {
            "jmeno": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Zadejte křestní jméno",
            }),
            "prijmeni": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Zadejte příjmení",
            }),
            "email": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Zadejte e-mail",
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        heslo1 = cleaned_data.get("heslo1")
        heslo2 = cleaned_data.get("heslo2")
        if heslo1 and heslo2 and heslo1 != heslo2:
            raise forms.ValidationError("Hesla se neshodují")
        return cleaned_data

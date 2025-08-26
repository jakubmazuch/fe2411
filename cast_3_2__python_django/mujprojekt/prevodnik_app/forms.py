from django import forms

JEDNOTKY = [
    ('m', 'metry'),
    ('cm', 'centimetry'),
    ('inch', 'palce'),
    ('ft', 'stopy'),
    ('yd', 'yardy')
]


class PrevodForm(forms.Form):
    hodnota = forms.FloatField(label='Zadej hodnotu')
    jednotka_od = forms.ChoiceField(choices=JEDNOTKY, label='Z')
    jednotka_do = forms.ChoiceField(choices=JEDNOTKY, label='Na')

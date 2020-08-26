from django import forms
from . import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class RaumForm(forms.ModelForm):
    class Meta:
        model = models.Raum
        fields = [
            "Raumnummer",
            "Anzahl_Sitzplaetze",
            "Beamer",
            "Whiteboard",
        ]


class ZeitraumForm(forms.ModelForm):
    class Meta:
        model = models.Zeitraum
        fields = [
            "Vorlesungszeit",
            "EndTime",
            "Datum",
            "StartTime",
        ]


class RaumbelegungForm(forms.ModelForm):
    class Meta:
        model = models.Raumbelegung
        fields = [
            "Belegt",
            "Belegungsgrund",
        ]



class RaumSearchForm(forms.ModelForm):
    Raumnummer = forms.CharField(max_length=32, required=False)
    Anzahl_Sitzplaetze = forms.CharField(max_length=32, required=False)
    
    

    class Meta:
        model = models.Raum
        fields = [
            "Raumnummer",
            "Anzahl_Sitzplaetze",
           
        ]

class BuchungForm(forms.ModelForm):

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit","Save"))



    class Meta:
        model = models.Buchung
        fields = "__all__"


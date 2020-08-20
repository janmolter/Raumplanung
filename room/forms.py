from django import forms
from . import models


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
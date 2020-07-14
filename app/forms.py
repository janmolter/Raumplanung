from django import forms
from .models import Raum, Zeitraum, Raumbelegung


class RaumForm(forms.ModelForm):
    class Meta:
        model = Raum
        fields = ['Raumnummer', 'Anzahl_Sitzplaetze', 'Beamer', 'Whiteboard']


class ZeitraumForm(forms.ModelForm):
    class Meta:
        model = Zeitraum
        fields = ['Datum', 'Vorlesungszeit', 'Dauer']


class RaumbelegungForm(forms.ModelForm):
    class Meta:
        model = Raumbelegung
        fields = ['Belegungsgrund', 'Belegt', 'Buchungszeitraum', 'Gebuchterraum', 'Benutzer']



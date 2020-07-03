from django import forms
from .models import WebseiteRaumbelegung, Person, Admin, User, Raum, Zeitraum, Raumbelegung


class WebseiteRaumbelegungForm(forms.ModelForm):
    class Meta:
        model = WebseiteRaumbelegung
        fields = ['name_room', 'Websiteraumbelegung_to_Person', 'Webseiteraumbelegung_to_Raum']


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name_person', 'Person_to_Admin']


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['firstname', 'lastname', 'Admin_to_Person', 'Admin_to_User', 'Admin_to_Raum', 'Admin_to_Raumbelegung']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'User_to_Person', 'User_to_admin', 'User_to_Raumbelegung']


class RaumForm(forms.ModelForm):
    class Meta:
        model = Raum
        fields = ['Belegt', 'Raumnummer', 'Anzahl_Sitzplätze', 'Beamer', 'Whiteboard', 'Raum_to_Admin', 'Raum_to_user', 'Raum_to_Zeitraum', 'Raum_to_Raumbelegung']


class ZeitraumForm(forms.ModelForm):
    class Meta:
        model = Zeitraum
        fields = ['Datum', 'Vorlesungszeit', 'Dauer', 'Zeitraum_to_Raumbelegung']


class RaumbelegungForm(forms.ModelForm):
    class Meta:
        model = Raumbelegung
        fields = ['name', 'Belegungsgrund', 'Raumbelegung_to_Zeitraum', 'Raumbelegung_to_Admin', 'Raumbelegung_to_user']



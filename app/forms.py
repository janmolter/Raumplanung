from django import forms
from .models import Raumbelegung, Person, Admin, User


class RaumbelegungForm(forms.ModelForm):
    class Meta:
        model = Raumbelegung
        fields = ['name_room', 'Raumbelegung_to_Person']


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name_person']


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['firstname', 'lastname', 'Admin_to_Person']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'User_to_Person']



from django.contrib import admin
from django import forms
from .models import Raum, Zeitraum, Raumbelegung

class RaumAdminForm(forms.ModelForm):

    class Meta:
        model = Raum
        fields = '__all__'


class RaumAdmin(admin.ModelAdmin):
    form = RaumAdminForm
    list_display = ['Raumnummer', 'Anzahl_Sitzplaetze', 'Beamer', 'Whiteboard']
    readonly_fields = ['Raumnummer', 'Anzahl_Sitzplaetze', 'Beamer', 'Whiteboard']

admin.site.register(Raum, RaumAdmin)


class ZeitraumAdminForm(forms.ModelForm):

    class Meta:
        model = Zeitraum
        fields = '__all__'


class ZeitraumAdmin(admin.ModelAdmin):
    form = ZeitraumAdminForm
    list_display = ['Datum', 'Vorlesungszeit', 'Dauer']
    readonly_fields = ['Datum', 'Vorlesungszeit', 'Dauer']

admin.site.register(Zeitraum, ZeitraumAdmin)


class RaumbelegungAdminForm(forms.ModelForm):

    class Meta:
        model = Raumbelegung
        fields = '__all__'


class RaumbelegungAdmin(admin.ModelAdmin):
    form = RaumbelegungAdminForm
    list_display = ['Belegungsgrund', 'Belegt']
    readonly_fields = ['Belegungsgrund', 'Belegt']

admin.site.register(Raumbelegung, RaumbelegungAdmin)



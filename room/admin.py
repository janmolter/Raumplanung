from django.contrib import admin
from django import forms

from . import models


class RaumAdminForm(forms.ModelForm):

    class Meta:
        model = models.Raum
        fields = "__all__"


class RaumAdmin(admin.ModelAdmin):
    form = RaumAdminForm
    list_display = [
        "Raumnummer",
        "Anzahl_Sitzplaetze",
        "Beamer",
        "Whiteboard",
    ]
    readonly_fields = [
       
    ]


class ZeitraumAdminForm(forms.ModelForm):

    class Meta:
        model = models.Zeitraum
        fields = "__all__"


class ZeitraumAdmin(admin.ModelAdmin):
    form = ZeitraumAdminForm
    list_display = [
        "Vorlesungszeit",
        "EndTime",
        "Datum",
        "StartTime",
    ]
    readonly_fields = [
        "Vorlesungszeit",
        "EndTime",
        "Datum",
        "StartTime",
    ]


class RaumbelegungAdminForm(forms.ModelForm):

    class Meta:
        model = models.Raumbelegung
        fields = "__all__"


class RaumbelegungAdmin(admin.ModelAdmin):
    form = RaumbelegungAdminForm
    list_display = [
        "Belegt",
        "Belegungsgrund",
    ]
    readonly_fields = [
        "Belegt",
        "Belegungsgrund",
    ]


admin.site.register(models.Raum, RaumAdmin)
admin.site.register(models.Zeitraum, ZeitraumAdmin)
admin.site.register(models.Raumbelegung, RaumbelegungAdmin)

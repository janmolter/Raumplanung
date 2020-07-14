from . import models

from rest_framework import serializers


class RaumSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Raum
        fields = (
            'pk', 
            'Raumnummer', 
            'Anzahl_Sitzplaetze', 
            'Beamer', 
            'Whiteboard', 
        )


class ZeitraumSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Zeitraum
        fields = (
            'pk', 
            'Datum', 
            'Vorlesungszeit', 
            'Dauer', 
        )


class RaumbelegungSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Raumbelegung
        fields = (
            'pk', 
            'Belegungsgrund', 
            'Belegt', 
        )



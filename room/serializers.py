from rest_framework import serializers

from . import models


class RaumSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Raum
        fields = [
            "Raumnummer",
            "Anzahl_Sitzplaetze",
            "Beamer",
            "Whiteboard",
        ]

class ZeitraumSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Zeitraum
        fields = [
            "Vorlesungszeit",
            "EndTime",
            "Datum",
            "StartTime",
        ]

class RaumbelegungSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Raumbelegung
        fields = [
            "Belegt",
            "Belegungsgrund",
        ]

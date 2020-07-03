from . import models

from rest_framework import serializers


class WebseiteRaumbelegungSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.WebseiteRaumbelegung
        fields = (
            'pk', 
            'name_room', 
        )


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Person
        fields = (
            'pk', 
            'name_person', 
        )


class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Admin
        fields = (
            'pk', 
            'firstname', 
            'lastname', 
        )


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'pk', 
            'firstname', 
            'lastname', 
        )


class RaumSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Raum
        fields = (
            'pk', 
            'Belegt', 
            'Raumnummer', 
            'Anzahl_Sitzplätze', 
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
            'name', 
            'Belegungsgrund', 
        )



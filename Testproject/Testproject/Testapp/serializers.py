from . import models

from rest_framework import serializers


class RaumbelegungSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Raumbelegung
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



from . import models
from . import serializers
from rest_framework import viewsets, permissions


class WebseiteRaumbelegungViewSet(viewsets.ModelViewSet):
    """ViewSet for the WebseiteRaumbelegung class"""

    queryset = models.WebseiteRaumbelegung.objects.all()
    serializer_class = serializers.WebseiteRaumbelegungSerializer
    permission_classes = [permissions.IsAuthenticated]


class PersonViewSet(viewsets.ModelViewSet):
    """ViewSet for the Person class"""

    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    permission_classes = [permissions.IsAuthenticated]


class AdminViewSet(viewsets.ModelViewSet):
    """ViewSet for the Admin class"""

    queryset = models.Admin.objects.all()
    serializer_class = serializers.AdminSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for the User class"""

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class RaumViewSet(viewsets.ModelViewSet):
    """ViewSet for the Raum class"""

    queryset = models.Raum.objects.all()
    serializer_class = serializers.RaumSerializer
    permission_classes = [permissions.IsAuthenticated]


class ZeitraumViewSet(viewsets.ModelViewSet):
    """ViewSet for the Zeitraum class"""

    queryset = models.Zeitraum.objects.all()
    serializer_class = serializers.ZeitraumSerializer
    permission_classes = [permissions.IsAuthenticated]


class RaumbelegungViewSet(viewsets.ModelViewSet):
    """ViewSet for the Raumbelegung class"""

    queryset = models.Raumbelegung.objects.all()
    serializer_class = serializers.RaumbelegungSerializer
    permission_classes = [permissions.IsAuthenticated]



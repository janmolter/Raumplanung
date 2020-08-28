from rest_framework import viewsets, permissions

from . import serializers
from . import models


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

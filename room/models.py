from django.db import models
from django.urls import reverse


class Raum(models.Model):

    # Fields
    Raumnummer = models.CharField(max_length=255)
    Anzahl_Sitzplaetze = models.IntegerField()
    Beamer = models.BooleanField()
    Whiteboard = models.BooleanField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("room_Raum_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("room_Raum_update", args=(self.pk,))


class Zeitraum(models.Model):

    # Fields
    Vorlesungszeit = models.TimeField()
    EndTime = models.DateTimeField()
    Datum = models.DateField()
    StartTime = models.DateTimeField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("room_Zeitraum_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("room_Zeitraum_update", args=(self.pk,))


class Raumbelegung(models.Model):

    # Fields
    Belegt = models.BooleanField()
    Belegungsgrund = models.CharField(max_length=255)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("room_Raumbelegung_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("room_Raumbelegung_update", args=(self.pk,))

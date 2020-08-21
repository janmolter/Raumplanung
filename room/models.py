from django.db import models
from django.urls import reverse
from django.conf import settings

class Raum(models.Model):

    # Fields
    Raumnummer = models.CharField(max_length=255)
    Anzahl_Sitzplaetze = models.IntegerField()
    Beamer = models.BooleanField()
    Whiteboard = models.BooleanField()

    class Meta:
        pass

    def __str__(self):
        return f'Raum {self.Raumnummer} mit {self.Anzahl_Sitzplaetze} Sitzplätzen'

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
        return f'{self.Datum} Zeitraum von {self.StartTime} bis {self.EndTime} '

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


class Buchung(models.Model):

    User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    Room = models.ForeignKey(Raum, on_delete = models.CASCADE)
    Check_in = models.ManyToManyField(Zeitraum)

    class Meta:
        pass

    def __str__(self):
        return f'{self.User} hat {self.Room} am {self.Check_in} gebucht'

    def get_absolute_url(self):
        return reverse("room_Buchen_detail", args=(self.pk,))



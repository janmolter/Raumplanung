from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.exceptions import ValidationError

class Raum(models.Model):

    # Fields
    Raumnummer = models.CharField(unique=True,max_length=255)
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
        return f'Zeitraum: {self.StartTime} -- Dauer: 90 Minuten  '

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

    User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE,unique=True, blank=True, null=True)
    Room = models.ForeignKey(Raum, on_delete = models.CASCADE,blank=True, null=True)
    Check_in = models.ForeignKey(Zeitraum,  on_delete = models.CASCADE, blank=True, null=True)

    class Meta:
        unique_together = ['Room', 'Check_in']
        pass

    def __str__(self):
        return f'{self.User} hat {self.Room} für den {self.Check_in.Datum} um {self.Check_in.Vorlesungszeit} für 90 Minuten gebucht'

    def get_absolute_url(self):
        return reverse("room_Buchen_detail", args=(self.pk,))
    




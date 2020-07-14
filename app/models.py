from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.contrib.postgres.fields.ranges import DateTimeRangeField
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateField
from django.db.models import IntegerField
from django.db.models import TimeField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Raum(models.Model):

    # Fields
    Raumnummer = models.CharField()
    Anzahl_Sitzplaetze = models.IntegerField()
    Beamer = models.BooleanField()
    Whiteboard = models.BooleanField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('App_raum_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('App_raum_update', args=(self.pk,))


class Zeitraum(models.Model):

    # Fields
    Datum = models.DateField()
    Vorlesungszeit = models.TimeField()
    Dauer = DateTimeRangeField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('App_zeitraum_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('App_zeitraum_update', args=(self.pk,))


class Raumbelegung(models.Model):

    # Fields
    Belegungsgrund = models.CharField(max_length=30)
    Belegt = models.BooleanField()

    # Relationship Fields
    Buchungszeitraum = models.ManyToManyField(
        'App.Zeitraum',
        related_name="raumbelegungs", 
    )
    Gebuchterraum = models.ForeignKey(
        'App.Raum',
        on_delete=models.CASCADE, related_name="raumbelegungs", 
    )
    Benutzer = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="raumbelegungs", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('App_raumbelegung_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('App_raumbelegung_update', args=(self.pk,))



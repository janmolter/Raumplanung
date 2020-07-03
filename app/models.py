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


class WebseiteRaumbelegung(models.Model):

    # Fields
    name_room = models.CharField(max_length=100)

    # Relationship Fields
    Websiteraumbelegung_to_Person = models.ForeignKey(
        'App.Person',
        on_delete=models.CASCADE, related_name="webseiteraumbelegungs", 
    )
    Webseiteraumbelegung_to_Raum = models.ForeignKey(
        'App.Raum',
        on_delete=models.CASCADE, related_name="webseiteraumbelegungs", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('App_webseiteraumbelegung_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('App_webseiteraumbelegung_update', args=(self.pk,))


class Person(models.Model):

    # Fields
    name_person = models.CharField(max_length=255)

    # Relationship Fields
    Person_to_Admin = models.OneToOneField(
        'App.Admin',
        on_delete=models.CASCADE, related_name="persons", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('App_person_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('App_person_update', args=(self.pk,))


class Admin(models.Model):

    # Fields
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=100)

    # Relationship Fields
    Admin_to_Person = models.OneToOneField(
        'App.Person',
        on_delete=models.CASCADE, related_name="admins", 
    )
    Admin_to_User = models.ManyToManyField(
        'App.User',
        related_name="admins", 
    )
    Admin_to_Raum = models.ManyToManyField(
        'App.Raum',
        related_name="admins", 
    )
    Admin_to_Raumbelegung = models.ManyToManyField(
        'App.Raumbelegung',
        related_name="admins", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('App_admin_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('App_admin_update', args=(self.pk,))


class User(models.Model):

    # Fields
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=100)

    # Relationship Fields
    User_to_Person = models.OneToOneField(
        'App.Person',
        on_delete=models.CASCADE, related_name="users", 
    )
    User_to_admin = models.ManyToManyField(
        'App.Admin',
        related_name="users", 
    )
    User_to_Raumbelegung = models.OneToOneField(
        'App.Raumbelegung',
        on_delete=models.CASCADE, related_name="users", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('App_user_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('App_user_update', args=(self.pk,))


class Raum(models.Model):

    # Fields
    Belegt = models.BooleanField()
    Raumnummer = models.CharField()
    Anzahl_Sitzplaetze = models.IntegerField()
    Beamer = models.BooleanField()
    Whiteboard = models.BooleanField()

    # Relationship Fields
    Raum_to_Admin = models.ManyToManyField(
        'App.Admin',
        related_name="raums", 
    )
    Raum_to_user = models.ForeignKey(
        'App.User',
        on_delete=models.CASCADE, related_name="raums", 
    )
    Raum_to_Zeitraum = models.ForeignKey(
        'App.Zeitraum',
        on_delete=models.CASCADE, related_name="raums", 
    )
    Raum_to_Raumbelegung = models.ForeignKey(
        'App.Raumbelegung',
        on_delete=models.CASCADE, related_name="raums", 
    )

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

    # Relationship Fields
    Zeitraum_to_Raumbelegung = models.OneToOneField(
        'App.Raumbelegung',
        on_delete=models.CASCADE, related_name="zeitraums", 
    )

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
    name = models.CharField(max_length=30)
    Belegungsgrund = models.CharField(max_length=30)

    # Relationship Fields
    Raumbelegung_to_Zeitraum = models.OneToOneField(
        'App.Zeitraum',
        on_delete=models.CASCADE, related_name="raumbelegungs", 
    )
    Raumbelegung_to_Admin = models.ManyToManyField(
        'App.Admin',
        related_name="raumbelegungs", 
    )
    Raumbelegung_to_user = models.OneToOneField(
        'App.User',
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



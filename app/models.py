from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import TextField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Raumbelegung(models.Model):

    # Fields
    name_room = models.TextField(max_length=100)

    # Relationship Fields
    Raumbelegung_to_Person = models.ForeignKey(
        'app.Person',
        on_delete=models.CASCADE, related_name="raumbelegungs", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('app_raumbelegung_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('app_raumbelegung_update', args=(self.pk,))


class Person(models.Model):

    # Fields
    name_person = models.CharField(max_length=255)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('app_person_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('app_person_update', args=(self.pk,))


class Admin(models.Model):

    # Fields
    firstname = models.CharField(max_length=255)
    lastname = models.TextField(max_length=100)

    # Relationship Fields
    Admin_to_Person = models.OneToOneField(
        'app.Person',
        on_delete=models.CASCADE, related_name="admins", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('app_admin_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('app_admin_update', args=(self.pk,))


class User(models.Model):

    # Fields
    firstname = models.CharField(max_length=255)
    lastname = models.TextField(max_length=100)

    # Relationship Fields
    User_to_Person = models.OneToOneField(
        'app.Person',
        on_delete=models.CASCADE, related_name="users", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('app_user_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('app_user_update', args=(self.pk,))



import unittest
from django.urls import reverse
from django.test import Client
from .models import Raum, Zeitraum, Raumbelegung
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_raum(**kwargs):
    defaults = {}
    defaults["Raumnummer"] = "Raumnummer"
    defaults["Anzahl_Sitzplaetze"] = "Anzahl_Sitzplaetze"
    defaults["Beamer"] = "Beamer"
    defaults["Whiteboard"] = "Whiteboard"
    defaults.update(**kwargs)
    return Raum.objects.create(**defaults)


def create_zeitraum(**kwargs):
    defaults = {}
    defaults["Datum"] = "Datum"
    defaults["Vorlesungszeit"] = "Vorlesungszeit"
    defaults["Dauer"] = "Dauer"
    defaults.update(**kwargs)
    return Zeitraum.objects.create(**defaults)


def create_raumbelegung(**kwargs):
    defaults = {}
    defaults["Belegungsgrund"] = "Belegungsgrund"
    defaults["Belegt"] = "Belegt"
    defaults.update(**kwargs)
    if "Buchungszeitraum" not in defaults:
        defaults["Buchungszeitraum"] = create_zeitraum()
    if "Gebuchterraum" not in defaults:
        defaults["Gebuchterraum"] = create_raum()
    if "Benutzer" not in defaults:
        defaults["Benutzer"] = create_django_contrib_auth_models_user()
    return Raumbelegung.objects.create(**defaults)


class RaumViewTest(unittest.TestCase):
    '''
    Tests for Raum
    '''
    def setUp(self):
        self.client = Client()

    def test_list_raum(self):
        url = reverse('App_raum_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_raum(self):
        url = reverse('App_raum_create')
        data = {
            "Raumnummer": "Raumnummer",
            "Anzahl_Sitzplaetze": "Anzahl_Sitzplaetze",
            "Beamer": "Beamer",
            "Whiteboard": "Whiteboard",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_raum(self):
        raum = create_raum()
        url = reverse('App_raum_detail', args=[raum.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_raum(self):
        raum = create_raum()
        data = {
            "Raumnummer": "Raumnummer",
            "Anzahl_Sitzplaetze": "Anzahl_Sitzplaetze",
            "Beamer": "Beamer",
            "Whiteboard": "Whiteboard",
        }
        url = reverse('App_raum_update', args=[raum.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ZeitraumViewTest(unittest.TestCase):
    '''
    Tests for Zeitraum
    '''
    def setUp(self):
        self.client = Client()

    def test_list_zeitraum(self):
        url = reverse('App_zeitraum_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_zeitraum(self):
        url = reverse('App_zeitraum_create')
        data = {
            "Datum": "Datum",
            "Vorlesungszeit": "Vorlesungszeit",
            "Dauer": "Dauer",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_zeitraum(self):
        zeitraum = create_zeitraum()
        url = reverse('App_zeitraum_detail', args=[zeitraum.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_zeitraum(self):
        zeitraum = create_zeitraum()
        data = {
            "Datum": "Datum",
            "Vorlesungszeit": "Vorlesungszeit",
            "Dauer": "Dauer",
        }
        url = reverse('App_zeitraum_update', args=[zeitraum.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class RaumbelegungViewTest(unittest.TestCase):
    '''
    Tests for Raumbelegung
    '''
    def setUp(self):
        self.client = Client()

    def test_list_raumbelegung(self):
        url = reverse('App_raumbelegung_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_raumbelegung(self):
        url = reverse('App_raumbelegung_create')
        data = {
            "Belegungsgrund": "Belegungsgrund",
            "Belegt": "Belegt",
            "Buchungszeitraum": create_zeitraum().pk,
            "Gebuchterraum": create_raum().pk,
            "Benutzer": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_raumbelegung(self):
        raumbelegung = create_raumbelegung()
        url = reverse('App_raumbelegung_detail', args=[raumbelegung.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_raumbelegung(self):
        raumbelegung = create_raumbelegung()
        data = {
            "Belegungsgrund": "Belegungsgrund",
            "Belegt": "Belegt",
            "Buchungszeitraum": create_zeitraum().pk,
            "Gebuchterraum": create_raum().pk,
            "Benutzer": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('App_raumbelegung_update', args=[raumbelegung.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)



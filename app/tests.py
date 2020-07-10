import unittest
from django.urls import reverse
from django.test import Client
from .models import WebseiteRaumbelegung, Person, Admin, User, Raum, Zeitraum, Raumbelegung
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


def create_webseiteraumbelegung(**kwargs):
    defaults = {}
    defaults["name_room"] = "name_room"
    defaults.update(**kwargs)
    if "Websiteraumbelegung_to_Person" not in defaults:
        defaults["Websiteraumbelegung_to_Person"] = create_person()
    if "Webseiteraumbelegung_to_Raum" not in defaults:
        defaults["Webseiteraumbelegung_to_Raum"] = create_raum()
    return WebseiteRaumbelegung.objects.create(**defaults)


def create_person(**kwargs):
    defaults = {}
    defaults["name_person"] = "name_person"
    defaults.update(**kwargs)
    if "Person_to_Admin" not in defaults:
        defaults["Person_to_Admin"] = create_admin()
    return Person.objects.create(**defaults)


def create_admin(**kwargs):
    defaults = {}
    defaults["firstname"] = "firstname"
    defaults["lastname"] = "lastname"
    defaults.update(**kwargs)
    if "Admin_to_Person" not in defaults:
        defaults["Admin_to_Person"] = create_person()
    if "Admin_to_User" not in defaults:
        defaults["Admin_to_User"] = create_user()
    if "Admin_to_Raum" not in defaults:
        defaults["Admin_to_Raum"] = create_raum()
    if "Admin_to_Raumbelegung" not in defaults:
        defaults["Admin_to_Raumbelegung"] = create_raumbelegung()
    return Admin.objects.create(**defaults)


def create_user(**kwargs):
    defaults = {}
    defaults["firstname"] = "firstname"
    defaults["lastname"] = "lastname"
    defaults.update(**kwargs)
    if "User_to_Person" not in defaults:
        defaults["User_to_Person"] = create_person()
    if "User_to_admin" not in defaults:
        defaults["User_to_admin"] = create_admin()
    if "User_to_Raumbelegung" not in defaults:
        defaults["User_to_Raumbelegung"] = create_raumbelegung()
    return User.objects.create(**defaults)


def create_raum(**kwargs):
    defaults = {}
    defaults["Belegt"] = "Belegt"
    defaults["Raumnummer"] = "Raumnummer"
    defaults["Anzahl_Sitzplaetze"] = "Anzahl_Sitzplaetze"
    defaults["Beamer"] = "Beamer"
    defaults["Whiteboard"] = "Whiteboard"
    defaults.update(**kwargs)
    if "Raum_to_Admin" not in defaults:
        defaults["Raum_to_Admin"] = create_admin()
    if "Raum_to_user" not in defaults:
        defaults["Raum_to_user"] = create_user()
    if "Raum_to_Zeitraum" not in defaults:
        defaults["Raum_to_Zeitraum"] = create_zeitraum()
    if "Raum_to_Raumbelegung" not in defaults:
        defaults["Raum_to_Raumbelegung"] = create_raumbelegung()
    return Raum.objects.create(**defaults)


def create_zeitraum(**kwargs):
    defaults = {}
    defaults["Datum"] = "Datum"
    defaults["Vorlesungszeit"] = "Vorlesungszeit"
    defaults["Dauer"] = "Dauer"
    defaults.update(**kwargs)
    if "Zeitraum_to_Raumbelegung" not in defaults:
        defaults["Zeitraum_to_Raumbelegung"] = create_raumbelegung()
    return Zeitraum.objects.create(**defaults)


def create_raumbelegung(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["Belegungsgrund"] = "Belegungsgrund"
    defaults.update(**kwargs)
    if "Raumbelegung_to_Zeitraum" not in defaults:
        defaults["Raumbelegung_to_Zeitraum"] = create_zeitraum()
    if "Raumbelegung_to_Admin" not in defaults:
        defaults["Raumbelegung_to_Admin"] = create_admin()
    if "Raumbelegung_to_user" not in defaults:
        defaults["Raumbelegung_to_user"] = create_user()
    return Raumbelegung.objects.create(**defaults)


class WebseiteRaumbelegungViewTest(unittest.TestCase):
    '''
    Tests for WebseiteRaumbelegung
    '''
    def setUp(self):
        self.client = Client()

    def test_list_webseiteraumbelegung(self):
        url = reverse('App_webseiteraumbelegung_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_webseiteraumbelegung(self):
        url = reverse('App_webseiteraumbelegung_create')
        data = {
            "name_room": "name_room",
            "Websiteraumbelegung_to_Person": create_person().pk,
            "Webseiteraumbelegung_to_Raum": create_raum().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_webseiteraumbelegung(self):
        webseiteraumbelegung = create_webseiteraumbelegung()
        url = reverse('App_webseiteraumbelegung_detail', args=[webseiteraumbelegung.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_webseiteraumbelegung(self):
        webseiteraumbelegung = create_webseiteraumbelegung()
        data = {
            "name_room": "name_room",
            "Websiteraumbelegung_to_Person": create_person().pk,
            "Webseiteraumbelegung_to_Raum": create_raum().pk,
        }
        url = reverse('App_webseiteraumbelegung_update', args=[webseiteraumbelegung.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PersonViewTest(unittest.TestCase):
    '''
    Tests for Person
    '''
    def setUp(self):
        self.client = Client()

    def test_list_person(self):
        url = reverse('App_person_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_person(self):
        url = reverse('App_person_create')
        data = {
            "name_person": "name_person",
            "Person_to_Admin": create_admin().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_person(self):
        person = create_person()
        url = reverse('App_person_detail', args=[person.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_person(self):
        person = create_person()
        data = {
            "name_person": "name_person",
            "Person_to_Admin": create_admin().pk,
        }
        url = reverse('App_person_update', args=[person.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AdminViewTest(unittest.TestCase):
    '''
    Tests for Admin
    '''
    def setUp(self):
        self.client = Client()

    def test_list_admin(self):
        url = reverse('App_admin_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_admin(self):
        url = reverse('App_admin_create')
        data = {
            "firstname": "firstname",
            "lastname": "lastname",
            "Admin_to_Person": create_person().pk,
            "Admin_to_User": create_user().pk,
            "Admin_to_Raum": create_raum().pk,
            "Admin_to_Raumbelegung": create_raumbelegung().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_admin(self):
        admin = create_admin()
        url = reverse('App_admin_detail', args=[admin.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_admin(self):
        admin = create_admin()
        data = {
            "firstname": "firstname",
            "lastname": "lastname",
            "Admin_to_Person": create_person().pk,
            "Admin_to_User": create_user().pk,
            "Admin_to_Raum": create_raum().pk,
            "Admin_to_Raumbelegung": create_raumbelegung().pk,
        }
        url = reverse('App_admin_update', args=[admin.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class UserViewTest(unittest.TestCase):
    '''
    Tests for User
    '''
    def setUp(self):
        self.client = Client()

    def test_list_user(self):
        url = reverse('App_user_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        url = reverse('App_user_create')
        data = {
            "firstname": "firstname",
            "lastname": "lastname",
            "User_to_Person": create_person().pk,
            "User_to_admin": create_admin().pk,
            "User_to_Raumbelegung": create_raumbelegung().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_user(self):
        user = create_user()
        url = reverse('App_user_detail', args=[user.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        user = create_user()
        data = {
            "firstname": "firstname",
            "lastname": "lastname",
            "User_to_Person": create_person().pk,
            "User_to_admin": create_admin().pk,
            "User_to_Raumbelegung": create_raumbelegung().pk,
        }
        url = reverse('App_user_update', args=[user.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


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
            "Belegt": "Belegt",
            "Raumnummer": "Raumnummer",
            "Anzahl_Sitzplaetze": "Anzahl_Sitzplaetze",
            "Beamer": "Beamer",
            "Whiteboard": "Whiteboard",
            "Raum_to_Admin": create_admin().pk,
            "Raum_to_user": create_user().pk,
            "Raum_to_Zeitraum": create_zeitraum().pk,
            "Raum_to_Raumbelegung": create_raumbelegung().pk,
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
            "Belegt": "Belegt",
            "Raumnummer": "Raumnummer",
            "Anzahl_Sitzplaetze": "Anzahl_Sitzplaetze",
            "Beamer": "Beamer",
            "Whiteboard": "Whiteboard",
            "Raum_to_Admin": create_admin().pk,
            "Raum_to_user": create_user().pk,
            "Raum_to_Zeitraum": create_zeitraum().pk,
            "Raum_to_Raumbelegung": create_raumbelegung().pk,
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
            "Zeitraum_to_Raumbelegung": create_raumbelegung().pk,
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
            "Zeitraum_to_Raumbelegung": create_raumbelegung().pk,
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
            "name": "name",
            "Belegungsgrund": "Belegungsgrund",
            "Raumbelegung_to_Zeitraum": create_zeitraum().pk,
            "Raumbelegung_to_Admin": create_admin().pk,
            "Raumbelegung_to_user": create_user().pk,
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
            "name": "name",
            "Belegungsgrund": "Belegungsgrund",
            "Raumbelegung_to_Zeitraum": create_zeitraum().pk,
            "Raumbelegung_to_Admin": create_admin().pk,
            "Raumbelegung_to_user": create_user().pk,
        }
        url = reverse('App_raumbelegung_update', args=[raumbelegung.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)



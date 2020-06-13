import unittest
from django.urls import reverse
from django.test import Client
from .models import Raumbelegung, Person, Admin, User
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


def create_raumbelegung(**kwargs):
    defaults = {}
    defaults["name_room"] = "name_room"
    defaults.update(**kwargs)
    if "Raumbelegung_to_Person" not in defaults:
        defaults["Raumbelegung_to_Person"] = create_person()
    return Raumbelegung.objects.create(**defaults)


def create_person(**kwargs):
    defaults = {}
    defaults["name_person"] = "name_person"
    defaults.update(**kwargs)
    return Person.objects.create(**defaults)


def create_admin(**kwargs):
    defaults = {}
    defaults["firstname"] = "firstname"
    defaults["lastname"] = "lastname"
    defaults.update(**kwargs)
    if "Admin_to_Person" not in defaults:
        defaults["Admin_to_Person"] = create_person()
    return Admin.objects.create(**defaults)


def create_user(**kwargs):
    defaults = {}
    defaults["firstname"] = "firstname"
    defaults["lastname"] = "lastname"
    defaults.update(**kwargs)
    if "User_to_Person" not in defaults:
        defaults["User_to_Person"] = create_person()
    return User.objects.create(**defaults)


class RaumbelegungViewTest(unittest.TestCase):
    '''
    Tests for Raumbelegung
    '''
    def setUp(self):
        self.client = Client()

    def test_list_raumbelegung(self):
        url = reverse('Testapp_raumbelegung_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_raumbelegung(self):
        url = reverse('Testapp_raumbelegung_create')
        data = {
            "name_room": "name_room",
            "Raumbelegung_to_Person": create_person().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_raumbelegung(self):
        raumbelegung = create_raumbelegung()
        url = reverse('Testapp_raumbelegung_detail', args=[raumbelegung.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_raumbelegung(self):
        raumbelegung = create_raumbelegung()
        data = {
            "name_room": "name_room",
            "Raumbelegung_to_Person": create_person().pk,
        }
        url = reverse('Testapp_raumbelegung_update', args=[raumbelegung.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PersonViewTest(unittest.TestCase):
    '''
    Tests for Person
    '''
    def setUp(self):
        self.client = Client()

    def test_list_person(self):
        url = reverse('Testapp_person_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_person(self):
        url = reverse('Testapp_person_create')
        data = {
            "name_person": "name_person",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_person(self):
        person = create_person()
        url = reverse('Testapp_person_detail', args=[person.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_person(self):
        person = create_person()
        data = {
            "name_person": "name_person",
        }
        url = reverse('Testapp_person_update', args=[person.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AdminViewTest(unittest.TestCase):
    '''
    Tests for Admin
    '''
    def setUp(self):
        self.client = Client()

    def test_list_admin(self):
        url = reverse('Testapp_admin_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_admin(self):
        url = reverse('Testapp_admin_create')
        data = {
            "firstname": "firstname",
            "lastname": "lastname",
            "Admin_to_Person": create_person().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_admin(self):
        admin = create_admin()
        url = reverse('Testapp_admin_detail', args=[admin.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_admin(self):
        admin = create_admin()
        data = {
            "firstname": "firstname",
            "lastname": "lastname",
            "Admin_to_Person": create_person().pk,
        }
        url = reverse('Testapp_admin_update', args=[admin.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class UserViewTest(unittest.TestCase):
    '''
    Tests for User
    '''
    def setUp(self):
        self.client = Client()

    def test_list_user(self):
        url = reverse('Testapp_user_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        url = reverse('Testapp_user_create')
        data = {
            "firstname": "firstname",
            "lastname": "lastname",
            "User_to_Person": create_person().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_user(self):
        user = create_user()
        url = reverse('Testapp_user_detail', args=[user.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        user = create_user()
        data = {
            "firstname": "firstname",
            "lastname": "lastname",
            "User_to_Person": create_person().pk,
        }
        url = reverse('Testapp_user_update', args=[user.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)



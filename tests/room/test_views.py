import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_Raum_list_view():
    instance1 = test_helpers.create_room_Raum()
    instance2 = test_helpers.create_room_Raum()
    client = Client()
    url = reverse("room_Raum_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Raum_create_view():
    client = Client()
    url = reverse("room_Raum_create")
    data = {
        "Raumnummer": "text",
        "Anzahl_Sitzplaetze": 1,
        "Beamer": true,
        "Whiteboard": true,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Raum_detail_view():
    client = Client()
    instance = test_helpers.create_room_Raum()
    url = reverse("room_Raum_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Raum_update_view():
    client = Client()
    instance = test_helpers.create_room_Raum()
    url = reverse("room_Raum_update", args=[instance.pk, ])
    data = {
        "Raumnummer": "text",
        "Anzahl_Sitzplaetze": 1,
        "Beamer": true,
        "Whiteboard": true,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Zeitraum_list_view():
    instance1 = test_helpers.create_room_Zeitraum()
    instance2 = test_helpers.create_room_Zeitraum()
    client = Client()
    url = reverse("room_Zeitraum_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Zeitraum_create_view():
    client = Client()
    url = reverse("room_Zeitraum_create")
    data = {
        "Vorlesungszeit": 100,
        "EndTime": datetime.now(),
        "Datum": datetime.now(),
        "StartTime": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Zeitraum_detail_view():
    client = Client()
    instance = test_helpers.create_room_Zeitraum()
    url = reverse("room_Zeitraum_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Zeitraum_update_view():
    client = Client()
    instance = test_helpers.create_room_Zeitraum()
    url = reverse("room_Zeitraum_update", args=[instance.pk, ])
    data = {
        "Vorlesungszeit": 100,
        "EndTime": datetime.now(),
        "Datum": datetime.now(),
        "StartTime": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Raumbelegung_list_view():
    instance1 = test_helpers.create_room_Raumbelegung()
    instance2 = test_helpers.create_room_Raumbelegung()
    client = Client()
    url = reverse("room_Raumbelegung_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Raumbelegung_create_view():
    client = Client()
    url = reverse("room_Raumbelegung_create")
    data = {
        "Belegt": true,
        "Belegungsgrund": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Raumbelegung_detail_view():
    client = Client()
    instance = test_helpers.create_room_Raumbelegung()
    url = reverse("room_Raumbelegung_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Raumbelegung_update_view():
    client = Client()
    instance = test_helpers.create_room_Raumbelegung()
    url = reverse("room_Raumbelegung_update", args=[instance.pk, ])
    data = {
        "Belegt": true,
        "Belegungsgrund": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302

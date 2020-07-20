import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from room import models as room_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_room_Raum(**kwargs):
    defaults = {}
    defaults["Raumnummer"] = ""
    defaults["Anzahl_Sitzplaetze"] = ""
    defaults["Beamer"] = ""
    defaults["Whiteboard"] = ""
    defaults.update(**kwargs)
    return room_models.Raum.objects.create(**defaults)
def create_room_Zeitraum(**kwargs):
    defaults = {}
    defaults["Vorlesungszeit"] = ""
    defaults["EndTime"] = datetime.now()
    defaults["Datum"] = datetime.now()
    defaults["StartTime"] = datetime.now()
    defaults.update(**kwargs)
    return room_models.Zeitraum.objects.create(**defaults)
def create_room_Raumbelegung(**kwargs):
    defaults = {}
    defaults["Belegt"] = ""
    defaults["Belegungsgrund"] = ""
    defaults.update(**kwargs)
    return room_models.Raumbelegung.objects.create(**defaults)

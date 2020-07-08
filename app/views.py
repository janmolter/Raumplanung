from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import WebseiteRaumbelegung, Person, Admin, User, Raum, Zeitraum, Raumbelegung
from .forms import WebseiteRaumbelegungForm, PersonForm, AdminForm, UserForm, RaumForm, ZeitraumForm, RaumbelegungForm
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hier wäre dann die Startseite")
 

class WebseiteRaumbelegungListView(ListView):
    model = WebseiteRaumbelegung


class WebseiteRaumbelegungCreateView(CreateView):
    model = WebseiteRaumbelegung
    form_class = WebseiteRaumbelegungForm


class WebseiteRaumbelegungDetailView(DetailView):
    model = WebseiteRaumbelegung


class WebseiteRaumbelegungUpdateView(UpdateView):
    model = WebseiteRaumbelegung
    form_class = WebseiteRaumbelegungForm


class PersonListView(ListView):
    model = Person


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm


class PersonDetailView(DetailView):
    model = Person


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm


class AdminListView(ListView):
    model = Admin


class AdminCreateView(CreateView):
    model = Admin
    form_class = AdminForm


class AdminDetailView(DetailView):
    model = Admin


class AdminUpdateView(UpdateView):
    model = Admin
    form_class = AdminForm


class UserListView(ListView):
    model = User


class UserCreateView(CreateView):
    model = User
    form_class = UserForm


class UserDetailView(DetailView):
    model = User


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm


class RaumListView(ListView):
    model = Raum


class RaumCreateView(CreateView):
    model = Raum
    form_class = RaumForm


class RaumDetailView(DetailView):
    model = Raum


class RaumUpdateView(UpdateView):
    model = Raum
    form_class = RaumForm


class ZeitraumListView(ListView):
    model = Zeitraum


class ZeitraumCreateView(CreateView):
    model = Zeitraum
    form_class = ZeitraumForm


class ZeitraumDetailView(DetailView):
    model = Zeitraum


class ZeitraumUpdateView(UpdateView):
    model = Zeitraum
    form_class = ZeitraumForm


class RaumbelegungListView(ListView):
    model = Raumbelegung


class RaumbelegungCreateView(CreateView):
    model = Raumbelegung
    form_class = RaumbelegungForm


class RaumbelegungDetailView(DetailView):
    model = Raumbelegung


class RaumbelegungUpdateView(UpdateView):
    model = Raumbelegung
    form_class = RaumbelegungForm


from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Raumbelegung, Person, Admin, User
from .forms import RaumbelegungForm, PersonForm, AdminForm, UserForm


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


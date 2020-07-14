from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Raum, Zeitraum, Raumbelegung
from .forms import RaumForm, ZeitraumForm, RaumbelegungForm


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


from django.views import generic
from . import models
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .filters import RaumFilter
from django_filters.views import FilterView




class RaumListView(generic.ListView):
    model = models.Raum
    form_class = forms.RaumForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = RaumFilter(self.request.GET, queryset=self.get_queryset())
        return context

class RaumSearchResultView(FilterView):
    model = models.Raum
    template_name = "room/Raum_list.html"


class RaumCreateView(generic.CreateView):
    model = models.Raum
    form_class = forms.RaumForm


class RaumDetailView(generic.DetailView):
    model = models.Raum
    form_class = forms.RaumForm


class RaumUpdateView(generic.UpdateView):
    model = models.Raum
    form_class = forms.RaumForm
    pk_url_kwarg = "pk"


class ZeitraumListView(generic.ListView):
    model = models.Zeitraum
    form_class = forms.ZeitraumForm


class ZeitraumCreateView(generic.CreateView):
    model = models.Zeitraum
    form_class = forms.ZeitraumForm


class ZeitraumDetailView(generic.DetailView):
    model = models.Zeitraum
    form_class = forms.ZeitraumForm


class ZeitraumUpdateView(generic.UpdateView):
    model = models.Zeitraum
    form_class = forms.ZeitraumForm
    pk_url_kwarg = "pk"


class RaumbelegungListView(generic.ListView):
    model = models.Raumbelegung
    form_class = forms.RaumbelegungForm


class RaumbelegungCreateView(generic.CreateView):
    model = models.Raumbelegung
    form_class = forms.RaumbelegungForm


class RaumbelegungDetailView(generic.DetailView):
    model = models.Raumbelegung
    form_class = forms.RaumbelegungForm


class RaumbelegungUpdateView(generic.UpdateView):
    model = models.Raumbelegung
    form_class = forms.RaumbelegungForm
    pk_url_kwarg = "pk"

class RaumbelegungSearch(generic.edit.FormView):
    template_name = "search.html"
    form_class = forms.RaumSearchForm
    success_url = "/room/room/Raum/"
    



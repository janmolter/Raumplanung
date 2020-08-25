from django.views import generic
from . import models
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .filters import RaumFilter
from django_filters.views import FilterView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required(login_url='/login/'),name='dispatch')
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


    
@method_decorator(login_required(login_url='/login/'),name='dispatch')

class RaumCreateView(generic.CreateView):
    model = models.Raum
    form_class = forms.RaumForm

@method_decorator(login_required(login_url='/login/'),name='dispatch')
class RaumDetailView(generic.DetailView):
    model = models.Raum
    form_class = forms.RaumForm

@method_decorator(login_required(login_url='/login/'),name='dispatch')
class RaumUpdateView(generic.UpdateView):
    model = models.Raum
    form_class = forms.RaumForm
    pk_url_kwarg = "pk"

@method_decorator(login_required(login_url='/login/'),name='dispatch')
class ZeitraumListView(generic.ListView):
    model = models.Zeitraum
    form_class = forms.ZeitraumForm

@method_decorator(login_required(login_url='/login/'),name='dispatch')
class ZeitraumCreateView(generic.CreateView):
    model = models.Zeitraum
    form_class = forms.ZeitraumForm

@method_decorator(login_required(login_url='/login/'),name='dispatch')
class ZeitraumDetailView(generic.DetailView):
    model = models.Zeitraum
    form_class = forms.ZeitraumForm

@method_decorator(login_required(login_url='/login/'),name='dispatch')
class ZeitraumUpdateView(generic.UpdateView):
    model = models.Zeitraum
    form_class = forms.ZeitraumForm
    pk_url_kwarg = "pk"

@method_decorator(login_required(login_url='/login/'),name='dispatch')
class RaumbelegungListView(generic.ListView):
    model = models.Raumbelegung
    form_class = forms.RaumbelegungForm

@method_decorator(login_required(login_url='/login/'),name='dispatch')
class RaumbelegungCreateView(generic.CreateView):
    model = models.Raumbelegung
    form_class = forms.RaumbelegungForm

@method_decorator(login_required(login_url='/login/'),name='dispatch')
class RaumbelegungDetailView(generic.DetailView):
    model = models.Raumbelegung
    form_class = forms.RaumbelegungForm

@method_decorator(login_required(login_url='/login/'),name='dispatch')
class RaumbelegungUpdateView(generic.UpdateView):
    model = models.Raumbelegung
    form_class = forms.RaumbelegungForm
    pk_url_kwarg = "pk"

class RaumbelegungSearch(generic.edit.FormView):
    template_name = "search.html"
    form_class = forms.RaumSearchForm
    success_url = "/room/room/Raum/"
    




@method_decorator(login_required(login_url='/login/'),name='dispatch')
class BuchungListView(generic.ListView):
    model = models.Buchung
    form_class = forms.BuchungForm

@method_decorator(login_required(login_url='/login/'),name='dispatch')
class BuchungCreateView(generic.CreateView):
    model = models.Buchung
    form_class = forms.BuchungForm

@method_decorator(login_required(login_url='/login/'),name='dispatch')
class BuchungDetailView(generic.DetailView):
    model = models.Buchung
    form_class = forms.BuchungForm

@method_decorator(login_required(login_url='/login/'),name='dispatch')
class BuchungUpdateView(generic.UpdateView):
    model = models.Buchung
    form_class = forms.BuchungForm
    pk_url_kwarg = "pk"


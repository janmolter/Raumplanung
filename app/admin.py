from django.contrib import admin
from django import forms
from .models import WebseiteRaumbelegung, Person, Admin, User, Raum, Zeitraum, Raumbelegung

class WebseiteRaumbelegungAdminForm(forms.ModelForm):

    class Meta:
        model = WebseiteRaumbelegung
        fields = '__all__'


class WebseiteRaumbelegungAdmin(admin.ModelAdmin):
    form = WebseiteRaumbelegungAdminForm
    list_display = ['name_room']
    readonly_fields = ['name_room']

admin.site.register(WebseiteRaumbelegung, WebseiteRaumbelegungAdmin)


class PersonAdminForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'


class PersonAdmin(admin.ModelAdmin):
    form = PersonAdminForm
    list_display = ['name_person']
    readonly_fields = ['name_person']

admin.site.register(Person, PersonAdmin)


class AdminAdminForm(forms.ModelForm):

    class Meta:
        model = Admin
        fields = '__all__'


class AdminAdmin(admin.ModelAdmin):
    form = AdminAdminForm
    list_display = ['firstname', 'lastname']
    readonly_fields = ['firstname', 'lastname']

admin.site.register(Admin, AdminAdmin)


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'


class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm
    list_display = ['firstname', 'lastname']
    readonly_fields = ['firstname', 'lastname']

admin.site.register(User, UserAdmin)


class RaumAdminForm(forms.ModelForm):

    class Meta:
        model = Raum
        fields = '__all__'


class RaumAdmin(admin.ModelAdmin):
    form = RaumAdminForm
    list_display = ['Belegt', 'Raumnummer', 'Anzahl_Sitzplätze', 'Beamer', 'Whiteboard']
    readonly_fields = ['Belegt', 'Raumnummer', 'Anzahl_Sitzplätze', 'Beamer', 'Whiteboard']

admin.site.register(Raum, RaumAdmin)


class ZeitraumAdminForm(forms.ModelForm):

    class Meta:
        model = Zeitraum
        fields = '__all__'


class ZeitraumAdmin(admin.ModelAdmin):
    form = ZeitraumAdminForm
    list_display = ['Datum', 'Vorlesungszeit', 'Dauer']
    readonly_fields = ['Datum', 'Vorlesungszeit', 'Dauer']

admin.site.register(Zeitraum, ZeitraumAdmin)


class RaumbelegungAdminForm(forms.ModelForm):

    class Meta:
        model = Raumbelegung
        fields = '__all__'


class RaumbelegungAdmin(admin.ModelAdmin):
    form = RaumbelegungAdminForm
    list_display = ['name', 'Belegungsgrund']
    readonly_fields = ['name', 'Belegungsgrund']

admin.site.register(Raumbelegung, RaumbelegungAdmin)



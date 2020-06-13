from django.contrib import admin
from django import forms
from .models import Raumbelegung, Person, Admin, User

class RaumbelegungAdminForm(forms.ModelForm):

    class Meta:
        model = Raumbelegung
        fields = '__all__'


class RaumbelegungAdmin(admin.ModelAdmin):
    form = RaumbelegungAdminForm
    list_display = ['name_room']
    readonly_fields = ['name_room']

admin.site.register(Raumbelegung, RaumbelegungAdmin)


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



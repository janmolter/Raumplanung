from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'raumbelegung', api.RaumbelegungViewSet)
router.register(r'person', api.PersonViewSet)
router.register(r'admin', api.AdminViewSet)
router.register(r'user', api.UserViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Raumbelegung
    path('Testapp/raumbelegung/', views.RaumbelegungListView.as_view(), name='Testapp_raumbelegung_list'),
    path('Testapp/raumbelegung/create/', views.RaumbelegungCreateView.as_view(), name='Testapp_raumbelegung_create'),
    path('Testapp/raumbelegung/detail/<int:pk>/', views.RaumbelegungDetailView.as_view(), name='Testapp_raumbelegung_detail'),
    path('Testapp/raumbelegung/update/<int:pk>/', views.RaumbelegungUpdateView.as_view(), name='Testapp_raumbelegung_update'),
)

urlpatterns += (
    # urls for Person
    path('Testapp/person/', views.PersonListView.as_view(), name='Testapp_person_list'),
    path('Testapp/person/create/', views.PersonCreateView.as_view(), name='Testapp_person_create'),
    path('Testapp/person/detail/<int:pk>/', views.PersonDetailView.as_view(), name='Testapp_person_detail'),
    path('Testapp/person/update/<int:pk>/', views.PersonUpdateView.as_view(), name='Testapp_person_update'),
)

urlpatterns += (
    # urls for Admin
    path('Testapp/admin/', views.AdminListView.as_view(), name='Testapp_admin_list'),
    path('Testapp/admin/create/', views.AdminCreateView.as_view(), name='Testapp_admin_create'),
    path('Testapp/admin/detail/<int:pk>/', views.AdminDetailView.as_view(), name='Testapp_admin_detail'),
    path('Testapp/admin/update/<int:pk>/', views.AdminUpdateView.as_view(), name='Testapp_admin_update'),
)

urlpatterns += (
    # urls for User
    path('Testapp/user/', views.UserListView.as_view(), name='Testapp_user_list'),
    path('Testapp/user/create/', views.UserCreateView.as_view(), name='Testapp_user_create'),
    path('Testapp/user/detail/<int:pk>/', views.UserDetailView.as_view(), name='Testapp_user_detail'),
    path('Testapp/user/update/<int:pk>/', views.UserUpdateView.as_view(), name='Testapp_user_update'),
)


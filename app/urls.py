from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'webseiteraumbelegung', api.WebseiteRaumbelegungViewSet)
router.register(r'person', api.PersonViewSet)
router.register(r'admin', api.AdminViewSet)
router.register(r'user', api.UserViewSet)
router.register(r'raum', api.RaumViewSet)
router.register(r'zeitraum', api.ZeitraumViewSet)
router.register(r'raumbelegung', api.RaumbelegungViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for WebseiteRaumbelegung
    path('App/webseiteraumbelegung/', views.WebseiteRaumbelegungListView.as_view(), name='App_webseiteraumbelegung_list'),
    path('App/webseiteraumbelegung/create/', views.WebseiteRaumbelegungCreateView.as_view(), name='App_webseiteraumbelegung_create'),
    path('App/webseiteraumbelegung/detail/<int:pk>/', views.WebseiteRaumbelegungDetailView.as_view(), name='App_webseiteraumbelegung_detail'),
    path('App/webseiteraumbelegung/update/<int:pk>/', views.WebseiteRaumbelegungUpdateView.as_view(), name='App_webseiteraumbelegung_update'),
)

urlpatterns += (
    # urls for Person
    path('App/person/', views.PersonListView.as_view(), name='App_person_list'),
    path('App/person/create/', views.PersonCreateView.as_view(), name='App_person_create'),
    path('App/person/detail/<int:pk>/', views.PersonDetailView.as_view(), name='App_person_detail'),
    path('App/person/update/<int:pk>/', views.PersonUpdateView.as_view(), name='App_person_update'),
)

urlpatterns += (
    # urls for Admin
    path('App/admin/', views.AdminListView.as_view(), name='App_admin_list'),
    path('App/admin/create/', views.AdminCreateView.as_view(), name='App_admin_create'),
    path('App/admin/detail/<int:pk>/', views.AdminDetailView.as_view(), name='App_admin_detail'),
    path('App/admin/update/<int:pk>/', views.AdminUpdateView.as_view(), name='App_admin_update'),
)

urlpatterns += (
    # urls for User
    path('App/user/', views.UserListView.as_view(), name='App_user_list'),
    path('App/user/create/', views.UserCreateView.as_view(), name='App_user_create'),
    path('App/user/detail/<int:pk>/', views.UserDetailView.as_view(), name='App_user_detail'),
    path('App/user/update/<int:pk>/', views.UserUpdateView.as_view(), name='App_user_update'),
)

urlpatterns += (
    # urls for Raum
    path('App/raum/', views.RaumListView.as_view(), name='App_raum_list'),
    path('App/raum/create/', views.RaumCreateView.as_view(), name='App_raum_create'),
    path('App/raum/detail/<int:pk>/', views.RaumDetailView.as_view(), name='App_raum_detail'),
    path('App/raum/update/<int:pk>/', views.RaumUpdateView.as_view(), name='App_raum_update'),
)

urlpatterns += (
    # urls for Zeitraum
    path('App/zeitraum/', views.ZeitraumListView.as_view(), name='App_zeitraum_list'),
    path('App/zeitraum/create/', views.ZeitraumCreateView.as_view(), name='App_zeitraum_create'),
    path('App/zeitraum/detail/<int:pk>/', views.ZeitraumDetailView.as_view(), name='App_zeitraum_detail'),
    path('App/zeitraum/update/<int:pk>/', views.ZeitraumUpdateView.as_view(), name='App_zeitraum_update'),
)

urlpatterns += (
    # urls for Raumbelegung
    path('App/raumbelegung/', views.RaumbelegungListView.as_view(), name='App_raumbelegung_list'),
    path('App/raumbelegung/create/', views.RaumbelegungCreateView.as_view(), name='App_raumbelegung_create'),
    path('App/raumbelegung/detail/<int:pk>/', views.RaumbelegungDetailView.as_view(), name='App_raumbelegung_detail'),
    path('App/raumbelegung/update/<int:pk>/', views.RaumbelegungUpdateView.as_view(), name='App_raumbelegung_update'),
)


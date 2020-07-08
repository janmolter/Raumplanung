from django.urls import path, include
from rest_framework import routers
from . import api
from . import views




router = routers.DefaultRouter()
router.register('webseiteraumbelegung', api.WebseiteRaumbelegungViewSet)
router.register('person', api.PersonViewSet)
router.register('admin', api.AdminViewSet)
router.register('user', api.UserViewSet)
router.register('raum', api.RaumViewSet)
router.register('zeitraum', api.ZeitraumViewSet)
router.register('raumbelegung', api.RaumbelegungViewSet)













urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for WebseiteRaumbelegung
    path('app/webseiteraumbelegung/', views.WebseiteRaumbelegungListView.as_view(), name='app_webseiteraumbelegung_list'),
    path('app/webseiteraumbelegung/create/', views.WebseiteRaumbelegungCreateView.as_view(), name='app_webseiteraumbelegung_create'),
    path('app/webseiteraumbelegung/detail/<int:pk>/', views.WebseiteRaumbelegungDetailView.as_view(), name='app_webseiteraumbelegung_detail'),
    path('app/webseiteraumbelegung/update/<int:pk>/', views.WebseiteRaumbelegungUpdateView.as_view(), name='app_webseiteraumbelegung_update'),
)

urlpatterns += (
    # urls for Person
    path('app/person/', views.PersonListView.as_view(), name='app_person_list'),
    path('app/person/create/', views.PersonCreateView.as_view(), name='app_person_create'),
    path('app/person/detail/<int:pk>/', views.PersonDetailView.as_view(), name='app_person_detail'),
    path('app/person/update/<int:pk>/', views.PersonUpdateView.as_view(), name='app_person_update'),
)

urlpatterns += (
    # urls for Admin
    path('app/admin/', views.AdminListView.as_view(), name='app_admin_list'),
    path('app/admin/create/', views.AdminCreateView.as_view(), name='app_admin_create'),
    path('app/admin/detail/<int:pk>/', views.AdminDetailView.as_view(), name='app_admin_detail'),
    path('app/admin/update/<int:pk>/', views.AdminUpdateView.as_view(), name='app_admin_update'),
)

urlpatterns += (
    # urls for User
    path('app/user/', views.UserListView.as_view(), name='app_user_list'),
    path('app/user/create/', views.UserCreateView.as_view(), name='app_user_create'),
    path('app/user/detail/<int:pk>/', views.UserDetailView.as_view(), name='app_user_detail'),
    path('app/user/update/<int:pk>/', views.UserUpdateView.as_view(), name='app_user_update'),
)

urlpatterns += (
    # urls for Raum
    path('app/raum/', views.RaumListView.as_view(), name='app_raum_list'),
    path('app/raum/create/', views.RaumCreateView.as_view(), name='app_raum_create'),
    path('app/raum/detail/<int:pk>/', views.RaumDetailView.as_view(), name='app_raum_detail'),
    path('app/raum/update/<int:pk>/', views.RaumUpdateView.as_view(), name='app_raum_update'),
)

urlpatterns += (
    # urls for Zeitraum
    path('app/zeitraum/', views.ZeitraumListView.as_view(), name='app_zeitraum_list'),
    path('app/zeitraum/create/', views.ZeitraumCreateView.as_view(), name='app_zeitraum_create'),
    path('app/zeitraum/detail/<int:pk>/', views.ZeitraumDetailView.as_view(), name='app_zeitraum_detail'),
    path('app/zeitraum/update/<int:pk>/', views.ZeitraumUpdateView.as_view(), name='app_zeitraum_update'),
)

urlpatterns += (
    # urls for Raumbelegung
    path('app/raumbelegung/', views.RaumbelegungListView.as_view(), name='app_raumbelegung_list'),
    path('app/raumbelegung/create/', views.RaumbelegungCreateView.as_view(), name='app_raumbelegung_create'),
    path('app/raumbelegung/detail/<int:pk>/', views.RaumbelegungDetailView.as_view(), name='app_raumbelegung_detail'),
    path('app/raumbelegung/update/<int:pk>/', views.RaumbelegungUpdateView.as_view(), name='app_raumbelegung_update'),
)

urlpatterns = (
    path('', views.index, name='index'),
)

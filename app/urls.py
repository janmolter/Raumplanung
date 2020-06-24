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
    path('raumbelegung/', views.RaumbelegungListView.as_view(), name='app_raumbelegung_list'),
    path('raumbelegung/create/', views.RaumbelegungCreateView.as_view(), name='app_raumbelegung_create'),
    path('raumbelegung/detail/<int:pk>/', views.RaumbelegungDetailView.as_view(), name='app_raumbelegung_detail'),
    path('raumbelegung/update/<int:pk>/', views.RaumbelegungUpdateView.as_view(), name='app_raumbelegung_update'),
)

urlpatterns += (
    # urls for Person
    path('person/', views.PersonListView.as_view(), name='app_person_list'),
    path('person/create/', views.PersonCreateView.as_view(), name='app_person_create'),
    path('person/detail/<int:pk>/', views.PersonDetailView.as_view(), name='app_person_detail'),
    path('person/update/<int:pk>/', views.PersonUpdateView.as_view(), name='app_person_update'),
)

urlpatterns += (
    # urls for Admin
    path('admin/', views.AdminListView.as_view(), name='app_admin_list'),
    path('admin/create/', views.AdminCreateView.as_view(), name='app_admin_create'),
    path('admin/detail/<int:pk>/', views.AdminDetailView.as_view(), name='app_admin_detail'),
    path('admin/update/<int:pk>/', views.AdminUpdateView.as_view(), name='app_admin_update'),
)

urlpatterns += (
    # urls for User
    path('user/', views.UserListView.as_view(), name='app_user_list'),
    path('user/create/', views.UserCreateView.as_view(), name='app_user_create'),
    path('user/detail/<int:pk>/', views.UserDetailView.as_view(), name='app_user_detail'),
    path('user/update/<int:pk>/', views.UserUpdateView.as_view(), name='app_user_update'),
)


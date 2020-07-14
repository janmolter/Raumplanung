from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'raum', api.RaumViewSet)
router.register(r'zeitraum', api.ZeitraumViewSet)
router.register(r'raumbelegung', api.RaumbelegungViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Raum
    path('app/raum/', views.RaumListView.as_view(), name='App_raum_list'),
    path('app/raum/create/', views.RaumCreateView.as_view(), name='App_raum_create'),
    path('app/raum/detail/<int:pk>/', views.RaumDetailView.as_view(), name='App_raum_detail'),
    path('app/raum/update/<int:pk>/', views.RaumUpdateView.as_view(), name='App_raum_update'),
)

urlpatterns += (
    # urls for Zeitraum
    path('app/zeitraum/', views.ZeitraumListView.as_view(), name='App_zeitraum_list'),
    path('app/zeitraum/create/', views.ZeitraumCreateView.as_view(), name='App_zeitraum_create'),
    path('app/zeitraum/detail/<int:pk>/', views.ZeitraumDetailView.as_view(), name='App_zeitraum_detail'),
    path('app/zeitraum/update/<int:pk>/', views.ZeitraumUpdateView.as_view(), name='App_zeitraum_update'),
)

urlpatterns += (
    # urls for Raumbelegung
    path('app/raumbelegung/', views.RaumbelegungListView.as_view(), name='App_raumbelegung_list'),
    path('app/raumbelegung/create/', views.RaumbelegungCreateView.as_view(), name='App_raumbelegung_create'),
    path('app/raumbelegung/detail/<int:pk>/', views.RaumbelegungDetailView.as_view(), name='App_raumbelegung_detail'),
    path('app/raumbelegung/update/<int:pk>/', views.RaumbelegungUpdateView.as_view(), name='App_raumbelegung_update'),
)


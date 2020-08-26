from django.urls import path, include
from rest_framework import routers
from django.views.generic import TemplateView
from . import api
from . import views


router = routers.DefaultRouter()
router.register("Raum", api.RaumViewSet)
router.register("Zeitraum", api.ZeitraumViewSet)
router.register("Raumbelegung", api.RaumbelegungViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("room/Raum/", views.RaumListView.as_view(), name="room_Raum_list"),
    path("room/Raum/create/", views.RaumCreateView.as_view(), name="room_Raum_create"),
    path("room/Raum/detail/<int:pk>/", views.RaumDetailView.as_view(), name="room_Raum_detail"),
    path("room/Raum/update/<int:pk>/", views.RaumUpdateView.as_view(), name="room_Raum_update"),
    path("room/Zeitraum/", views.ZeitraumListView.as_view(), name="room_Zeitraum_list"),
    path("room/Zeitraum/create/", views.ZeitraumCreateView.as_view(), name="room_Zeitraum_create"),
    path("room/Zeitraum/detail/<int:pk>/", views.ZeitraumDetailView.as_view(), name="room_Zeitraum_detail"),
    path("room/Zeitraum/update/<int:pk>/", views.ZeitraumUpdateView.as_view(), name="room_Zeitraum_update"),
    path("room/Raumbelegung/", views.RaumbelegungListView.as_view(), name="room_Raumbelegung_list"),
    path("room/Raumbelegung/create/", views.RaumbelegungCreateView.as_view(), name="room_Raumbelegung_create"),
    path("room/Raumbelegung/detail/<int:pk>/", views.RaumbelegungDetailView.as_view(), name="room_Raumbelegung_detail"),
    path("room/Raumbelegung/update/<int:pk>/", views.RaumbelegungUpdateView.as_view(), name="room_Raumbelegung_update"),
    
    path("room/buchen/", TemplateView.as_view(template_name='booking.html'), name='booking'),
    path("room/Kalender/",TemplateView.as_view(template_name='calender.html'), name='calender'), 
    path("room/suchen/",views.RaumbelegungSearch.as_view(), name='search'),
    path("room/suchen/result", views.RaumSearchResultView.as_view(), name='search_result'),

    path("room/Buchen/", views.BuchungListView.as_view(), name="room_Buchen_list"),
    path("room/Buchen/create/", views.BuchungCreateView.as_view(), name="room_Buchen_create"),
    path("room/Buchen/detail/<int:pk>/", views.BuchungDetailView.as_view(), name="room_Buchen_detail"),
    path("room/Buchen/update/<int:pk>/", views.BuchungUpdateView.as_view(), name="room_Buchen_update"),




)

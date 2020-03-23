from django.urls import path

from .views import ListLocations, DetailLocation, ListTrails, DetailTrails

urlpatterns = [
    path('<int:pk>/', DetailLocation.as_view()),
    path('', ListLocations.as_view()),
    path('trails/<int:pk>/', DetailTrails.as_view()),
    path('trails/', ListTrails.as_view()),
]

from django.urls import path

from .views import ListLocations, DetailLocation

urlpatterns = [
    path('<int:pk>/', DetailLocation.as_view()),
    path('', ListLocations.as_view()),
]

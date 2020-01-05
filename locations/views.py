from django.shortcuts import render
from rest_framework import generics

from .models import Location
from .serializers import LocationSerializer

# Create your views here.
class ListLocations(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class DetailLocation(generics.RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

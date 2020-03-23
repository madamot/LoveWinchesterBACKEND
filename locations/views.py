from django.shortcuts import render
from rest_framework import generics

from .models import Location, Trails
from .serializers import LocationSerializer, TrailsSerializer

# Create your views here.
class ListLocations(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class DetailLocation(generics.RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class ListTrails(generics.ListAPIView):
    queryset = Trails.objects.all()
    serializer_class = TrailsSerializer

class DetailTrails(generics.RetrieveAPIView):
    queryset = Trails.objects.all()
    serializer_class = TrailsSerializer

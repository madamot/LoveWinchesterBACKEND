from rest_framework import serializers
from .models import Location, Trails

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'image', 'type', 'description', 'latitude', 'longitude',)
        model = Location

class TrailsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'origin', 'destination', 'waypoints', 'image',)
        model = Trails
        depth = 1

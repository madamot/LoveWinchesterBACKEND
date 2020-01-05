from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'image', 'type', 'description', 'latitude', 'longitude',)
        model = Location

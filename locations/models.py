from django.db import models

# Create your models here.
class Location(models.Model):
    TYPE = (('Attraction', 'Attraction'), ('Commercial', 'Commercial'))
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=500)
    type = models.CharField(max_length=15, choices=TYPE)
    description = models.CharField(max_length=500, default='Check out the AR content!')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

class Trails(models.Model):
    name = models.CharField(max_length=50)
    origin = models.ForeignKey(
        Location, related_name="Origin", on_delete=models.CASCADE)
    destination = models.ForeignKey(
        Location, related_name="Destination", on_delete=models.CASCADE)
    waypoints = models.ForeignKey(
        Location, related_name="Waypoint", on_delete=models.CASCADE)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.name

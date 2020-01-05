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

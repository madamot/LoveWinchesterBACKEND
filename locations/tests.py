from django.test import TestCase

from .models import Location

# Create your tests here.

class LocationTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_location = Location.objects.create(
        name='Location Title', image='www.google.com', type='Attraction', description='Location Description...', latitude=51.060891, longitude=-1.313165)
        test_location.save()

    def test_location_content(self):
        location = Location.objects.get(id=1)
        expected_name = f'{location.name}'
        expected_image = f'{location.image}'
        expected_type = f'{location.type}'
        expected_description = f'{location.description}'
        expected_latitude = f'{location.latitude}'
        expected_longitude = f'{location.longitude}'
        self.assertEqual(expected_name, 'Location Title')
        self.assertEqual(expected_image, 'www.google.com')
        self.assertEqual(expected_type, 'Attraction')
        self.assertEqual(expected_description, 'Location Description...')
        self.assertEqual(expected_latitude, '51.060891')
        self.assertEqual(expected_longitude, '-1.313165')

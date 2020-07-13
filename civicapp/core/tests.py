from django.test import TestCase
from myapp.models import Animal

class ProfileTestCase(TestCase):
    def setUp(self):
        Profile.objects.create(name="lion", sound="roar")
        Profile.objects.create(name="cat", sound="meow")

    def test_profile_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
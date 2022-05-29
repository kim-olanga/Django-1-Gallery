from django.test import TestCase
from .models import Category, Location, Image

# Create your tests here.
class CategoryTestClass(TestCase):
    #set up method
    def setUp(self):
        self.new_category=Category(category = "test_category1")

    #instances
    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Category))

    #save method
    def test_save_method(self):
        self.new_category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

class LocationTestClass(TestCase):
    #set up method 
    def setUp(self):
        self.location=Location(location = "Location1")

    #instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    #save method
    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

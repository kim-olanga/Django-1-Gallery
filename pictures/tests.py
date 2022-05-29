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

class ImageTestClass(TestCase):
    def setUp(self):
        
        self.location = Location(location='Animation')
        self.location.save_location()

        self.category = Category(category='Animation')
        self.category.save_category()
        
        self.new_Image=Image(image = "image/minions.jpeg",name ="minions", description="Cartoon is not animation", location_id = self.location, category_id= self.category)

    def teardown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    #instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_Image,Image))

    #save method
    def test_save_method(self):
        self.new_Image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    #delete
    def test_deleteImage(self):
        self.new_Image.save_image()
        self.new_image2 = Image.objects.create(image ='image/minions.jpeg', name = 'Jpg image', description= 'jpg is an image format', location_id=self.location, category_id=self.category)
        Image.delete_image(self.new_Image.id)
        self.assertTrue(len(Image.objects.all())==1)

    #update 
    def test_updateImage(self):
        self.new_Image.save_image()
        self.new_Image.update_image(self.new_Image.id, 'image/minions.jpeg')
        new_updated_image = Image.objects.get(id=self.new_Image.id)
        self.assertEqual(new_updated_image.image, 'image/minions.jpeg')
    
    
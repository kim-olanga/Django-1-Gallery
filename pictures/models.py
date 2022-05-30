import datetime as dt
from distutils.command.upload import upload
from unicodedata import category
from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=200)

    def save_location(self):
        self.save()

    def __str__(self):
        return self.location

class Category(models.Model):
    category = models.CharField(max_length=200)

    def save_category(self):
        self.save()
        
    def __str__(self):
        return self.category

class Image(models.Model):
    image= models.ImageField(default ="default value")
    name =models.CharField(max_length=100)
    description =models.TextField()
    date_of_upload = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
        
    class Meta:
        ordering=['date_of_upload']
        
    def save_image(self):
        self.save()
        
    #delete
    @classmethod
    def delete_image(cls, id):
        cls.objects.filter(id=id).delete()
    
    #update    
    @classmethod
    def update_image(cls, id,updatedimage):
        cls.objects.filter(id=id).update(image=updatedimage)
    
    @classmethod
    def get_all_images(cls):
        images = Image.objects.all()
        return images
        
    @classmethod
    def get_image_by_id(cls,image_id):
        image=Image.objects.get(id=image_id)
        return image
    
    @classmethod
    def search_by_category(cls,search_term):
        images=Image.objects.filter(name__icontains=search_term)
        return images

    @classmethod
    def filter_by_location(cls,location_id):
        images=Image.objects.filter(id=location_id)
        return images

    @classmethod
    def filter_by_category(cls,category_id):
        images=Image.objects.filter(id=category_id)
        return images
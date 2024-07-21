from django.db import models
from django_summernote.fields import SummernoteTextField
from cloudinary.models import CloudinaryField

class MenuCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField('image', default='placeholder')
    
    def __str__(self):
        return self.name

from email.mime import image
import imp
from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField() #The Id Version of the name

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}'


class Products(models.model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True) #Automatically adds date when new product is added to the database
    
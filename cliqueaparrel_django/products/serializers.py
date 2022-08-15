import imp
from operator import imod

from rest_framework import serializers

from .models import Category, Products


#Create product serializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "get_image",
            "get_thumbnail",
        )

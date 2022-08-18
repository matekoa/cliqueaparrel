from itertools import product
from operator import imod

from rest_framework import serializers

from .models import Category, Product


#Create product serializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "price",
            "get_absolute_url",
            "description",
            "get_image",
            "get_thumbnail",
        )

class CategorySerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )
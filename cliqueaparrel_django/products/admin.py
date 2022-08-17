from django.contrib import admin

from .models import Category, Product


# Add products and categories to the admin backend
admin.site.register(Category)
admin.site.register(Product)
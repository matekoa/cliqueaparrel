from django.contrib import admin

from .models import Category, Products


# Add products and categories to the admin backend
admin.site.register(Category)
admin.site.register(Products)
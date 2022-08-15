from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Products
from .serializers import ProductSerializer


#Get The four latest Products
class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Products.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

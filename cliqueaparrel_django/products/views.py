from django.http import Http404

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

#View set for product details
class ProductDetail((APIView)):
    def get_object(self, category_slug, product_slug):
        try:
            return Products.objects.filter(category_slug=category_slug).get(slug=product_slug)
        
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, category_slug,product_slug, format=None):
        products = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(products)
        return Response(serializer.data)

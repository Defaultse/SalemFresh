from django.shortcuts import render
from rest_framework import generics, mixins
from core.models import *
from core.serializers import *


class CustomerApiView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ShopApiView(generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ProductApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryApiView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

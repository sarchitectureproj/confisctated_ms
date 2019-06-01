from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .models import Item, Category, Delivery
from .serializer import ItemSerializer,CategorySerializer,DeliverySerializer
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter


class ItemAPI(viewsets.ModelViewSet):
    __basic_fields = ('__all__')
    
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields
    

class CategoryAPI(viewsets.ModelViewSet):
    __basic_fields = ('__all__')

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields


class DeliveryAPI(viewsets.ModelViewSet):
    __basic_fields = ('__all__')
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields


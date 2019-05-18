from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .models import Item, Category, Delivery
from .serializer import ItemSerializer,CategorySerializer,DeliverySerializer
# Create your views here.

def index(request):
    return HttpResponse("Sucess")

class ItemAPI(viewsets.ModelViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer 
    
class CategoryAPI(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class DeliveryAPI(viewsets.ModelViewSet):

    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
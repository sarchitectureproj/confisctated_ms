from rest_framework import serializers,viewsets
from .models import Item,Category,Delivery


class ItemSerialiser(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'name', 'confiscation', 'weight', 'quiantity', 'category', 'passenger')
        
class CategorySerialiser(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'recoverable', 'delivery')

class DeliverySerialiser(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Delivery
        fields = ('id', 'open_time', 'close_time', 'description')
        
      
class ItemViewSet(viewsets.ModelViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerialiser   
    
class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerialiser
    
class DeliveryViewSet(viewsets.ModelViewSet):

    queryset = Delivery.objects.all()
    serializer_class = DeliverySerialiser

from rest_framework import serializers
from .models import Item,Category,Delivery


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('__all__')
        
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('__all__')

class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = ('__all__')
        

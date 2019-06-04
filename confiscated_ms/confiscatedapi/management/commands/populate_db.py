from django.core.management.base import BaseCommand
from confiscatedapi.models import Item, Delivery, Category
import random
import json

class Command(BaseCommand):
    help = 'Populate the database'

    def _create_deliveries(self):
        
        dataList = []
        with open('./seeds/delivery.json') as json_file:  
            dataList = json.load(json_file)
        
        for data in list(random.sample(dataList, k=20)):
            temp = Delivery(open_time=data["open_time"],close_time=data["close_time"],delivery_point=data["delivery_point"])
            temp.save()

    def _create_categories(self):
        dataList = []
        with open('./seeds/category.json') as json_file:  
            dataList = json.load(json_file)
        
        for data in list(random.sample(dataList, k=50)):
            temp = Category(name=data["name"][:20],description=data["description"][:100],recoverable=data["recoverable"],delivery=Delivery.objects.get(id=data["delivery"]))
            temp.save()

    def _create_items(self):
        dataList = []
        with open('./seeds/item.json') as json_file:  
            dataList = json.load(json_file)
        
        for data in list(random.sample(dataList, k=500)):
            temp = Item(name=data["name"],confiscation_date=data["confiscation_date"],units=data["units"],category=Category.objects.get(id=data["category"]),passenger=data["passenger"][:2])
            temp.save()
            
    def handle(self, *args, **options):
        Item.objects.all().delete()
        Category.objects.all().delete()
        Delivery.objects.all().delete()
        
        self._create_deliveries()
        self._create_categories()
        self._create_items()
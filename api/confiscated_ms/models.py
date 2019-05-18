from django.db import models
from django.utils import timezone
# Create your models here.

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    confiscation = models.DateTimeField()
    weight = models.FloatField(default=0)
    quiantity = models.IntegerField(default=1)
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
    )
    passenger = models.IntegerField(blank=False)

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255,blank=True)
    recoverable = models.BooleanField(default=True)
    delivery = models.ForeignKey(
        'Delivery',
        on_delete=models.SET_NULL,
        null=True,
    )

class Delivery(models.Model):
    id = models.AutoField(primary_key=True)
    open_time = models.TimeField()
    close_time = models.TimeField()
    description = models.CharField(max_length=255,blank=True,unique=True,null=True)
    

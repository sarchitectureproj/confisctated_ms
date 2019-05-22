from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    confiscation_date = models.DateField(null=True)
    confiscation_time = models.TimeField(null=True)
    quantity = models.IntegerField(default=1)
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
    )
    passenger = models.IntegerField(blank=False)
    def __str__(self):
        return self.name

class Category(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,unique=True)
    description = models.CharField(max_length=255,blank=True)
    recoverable = models.BooleanField(default=True)
    delivery = models.ForeignKey(
        'Delivery',
        on_delete=models.PROTECT,
        null=True,
    )
    
    def save(self, *args, **kwargs):
        if not self.recoverable:
            self.delivery = None
        super().save(*args, **kwargs)  # Call the "real" save() method.
    
    def __str__(self):
        return self.name
    
    

class Delivery(models.Model):

    DELIVERY_POINTS = [
        ('P01', 'Punto 01'),
        ('P02', 'Punto 02'),
        ('P03', 'Punto 03'),
        ('P04', 'Punto 04'),
        ('P05', 'Punto 05'),
    ]

    id = models.AutoField(primary_key=True)
    open_time = models.TimeField(null=False)
    close_time = models.TimeField(null=False)
    delivery_point = models.CharField(
        max_length=3,
        choices=DELIVERY_POINTS,
        default='P01')
    def __str__(self):
        return '%s: %s - %s' % (self.delivery_point, self.open_time, self.close_time)

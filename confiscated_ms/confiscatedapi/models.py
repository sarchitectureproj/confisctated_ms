from django.db import models
from django.utils import timezone
# Create your models here.

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    confiscation_date = models.DateField()
    confiscation_time = models.TimeField()
    weight = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
    )
    passenger = models.IntegerField(blank=False)
    def __str__(self):
        return self.name

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,unique=True)
    description = models.CharField(max_length=255,blank=True)
    recoverable = models.BooleanField(default=True)
    delivery = models.ForeignKey(
        'Delivery',
        on_delete=models.SET_NULL,
        null=True,
    )
    def __str__(self):
        return self.name

class Delivery(models.Model):

    DELIVERY_POINTS = [
        ('NNN', 'None'),
        ('PN1', 'Norte'),
        ('PC1', 'Centro'),
        ('PS1', 'Sur'),
        ('PC8', 'Cabina 08'),
    ]

    id = models.AutoField(primary_key=True)
    open_time = models.TimeField()
    close_time = models.TimeField()
    delivery_point = models.CharField(
        max_length=3,
        choices=DELIVERY_POINTS,
        default='NNN')
    def __str__(self):
        return self.delivery_point

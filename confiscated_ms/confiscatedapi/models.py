from django.db import models
from rest_framework import serializers
from django.utils import timezone
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.core.exceptions import ValidationError
# Create your models here.

def validate_date(value):
    if value > datetime.date.today() or value < datetime.date(2019, 1, 1):
        raise ValidationError('Date must be between 01-01-2019 and today',
            params={'value': value},
        )


class Item(models.Model):
    
    name = models.CharField(max_length=20)
    confiscation_date = models.DateField(validators=[validate_date])
    units = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
    )
    passenger = models.CharField(max_length=2)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('confiscation_date',)

class Category(models.Model):
    
    name = models.CharField(max_length=20,unique=True)
    description = models.CharField(max_length=100)
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
        
    class Meta:
        ordering = ('name',)
    
    

class Delivery(models.Model):

    open_time = models.TimeField()
    close_time = models.TimeField()
    delivery_point = models.CharField(
        max_length=20)

    def clean(self):
        if self.open_time >= self.close_time:
            raise serializers.ValidationError("Open time must be lower than Close time")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Delivery, self).save(*args, **kwargs)

    def __str__(self):
        return '%s: %s - %s' % (self.delivery_point, self.open_time, self.close_time)

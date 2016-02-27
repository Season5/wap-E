# from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Top_spots (models.Model):
    image = models.ImageField(upload_to='photos', verbose_name='My Photo')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    
class Popular (models.Model):
    image = models.ImageField(upload_to='photos', verbose_name='My Photo')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length = 500)
    contact = models.CharField(max_length=10)
    
class Content (models.Model):
    image = models.ImageField(upload_to='photos', verbose_name='My Photo')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    
    def publish(self):
        # self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.name
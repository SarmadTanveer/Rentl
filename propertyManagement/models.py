from django.db import models
from django.urls import reverse
from datetime import datetime

class Listing(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    #lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    main_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    list_data = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("listing_detail", args=[str(self.id)])
# Create your models here.

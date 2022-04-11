from pyexpat import model
from django.db import models
from django.urls import reverse
from datetime import datetime
from accounts.models import User,LandlordProfile, TenantProfile

class Listing(models.Model):

    class Meta: 
        permissions = (("can_edit","Update Listing"),("can_delete", "Delete Listing"),("can_create", "Create Listing"),)

    owner = models.ForeignKey(User,null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200,null=True, blank=True)
    city = models.CharField(max_length=100,null=True, blank=True)
    state = models.CharField(max_length=100,null=True, blank=True)
    zipcode = models.CharField(max_length=20,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    bedrooms = models.IntegerField(null=True, blank=True)
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1,null=True, blank=True)
    garage = models.IntegerField(default=0,null=True, blank=True)
    sqft = models.IntegerField(null=True, blank=True)
    #lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    main_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    list_data = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("listing_detail", args=[str(self.id)])


class LeaseOffPlatform(models.Model): 
    listing = models.OneToOneField(Listing, on_delete=models.CASCADE, primary_key=True)
    landlord = models.ForeignKey(LandlordProfile, on_delete=models.CASCADE)
    tenant_lastName = models.CharField(max_length=50)
    tenant_contact = models.IntegerField()
    tenant_firstName = models.CharField(max_length=50)
    leaseStartDate = models.DateField(auto_now=False,auto_now_add=False)
    leaseEndDate = models.DateField(auto_now=False,auto_now_add=False)
    Rent = models.DecimalField(max_digits=10,decimal_places=2)
    leaseDocument = models.FileField(upload_to='uploads/')
# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save

# Create your models here.
#User

class User(AbstractUser):
    is_tenant = models.BooleanField(default=False)
    is_landlord = models.BooleanField(default=False)
    phone_number = models.PositiveBigIntegerField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    profile_pic = models.ImageField(null=True, blank=True)

class LandlordProfile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='landlord_profile')

class TenantProfile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='tenant_profile')
    BankInstitutionNum = models.PositiveIntegerField(null=True, blank=True)
    BankTansitNum = models.PositiveIntegerField(null=True, blank=True)
    BankAccountNum = models.PositiveIntegerField(null=True, blank=True)
    landlordID = models.ForeignKey(LandlordProfile, models.SET_NULL,null=True, blank=True)




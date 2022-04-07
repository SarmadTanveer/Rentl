from django import forms 
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from .models import User, TenantProfile, LandlordProfile

class CustomUserChangeForm(UserChangeForm):

    class Meta: 
        model = User
        fields = ('username', 'email','is_tenant','is_landlord')

class TenantSignupForm(UserCreationForm): 
    BankInstitutionNum = forms.IntegerField(required=False)
    BankTansitNum = forms.IntegerField(required=False)
    BankAccountNum =forms.IntegerField(required=False)

    class Meta: 
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name','username', 'email', 'dob','profile_pic')
    
    @transaction.atomic
    def save(self): 
        user = super().save(commit=False)
        user.is_tenant = True
        user.save()
        tenant = TenantProfile.objects.create(user=user)
        tenant_group = Group.objects.get(name="Tenants")
        tenant_group.user_set.add(user)
        

        return user

class LandlordSignupForm(UserCreationForm):
    class Meta: 
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name','username', 'email', 'dob','profile_pic')
    
    @transaction.atomic
    def save(self): 
        user = super().save(commit=False)
        user.is_landlord = True
        user.save()
        landlord = LandlordProfile.objects.create(user=user)
        landlord_group = Group.objects.get(name="Landlords")
        landlord_group.user_set.add(user)
        return user
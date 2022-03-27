from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import TenantSignupForm, CustomUserChangeForm
from.models import User, LandlordProfile, TenantProfile

# Register your models here.

admin.site.register(User)
admin.site.register(LandlordProfile)
admin.site.register(TenantProfile)



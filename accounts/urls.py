from django.urls import path 
from .views import SignUpViewTenant, ProfileView, SignUpViewLandlord, LandlordProfileView, TenantProfileView

urlpatterns = [
    path('signup/tenant',SignUpViewTenant, name='tenant_signup'), 
    path('signup/landlord',SignUpViewLandlord,name='landlord_signup'),
    path('profile/', ProfileView, name='profile'), 
    path('landlordfacing/',LandlordProfileView, name='landlordProfile'), 
    path('tenantfacing/',TenantProfileView, name='tenantProfile')
]
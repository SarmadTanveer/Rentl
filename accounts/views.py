from audioop import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import TenantSignupForm, LandlordSignupForm

# Create your views here.
def SignUpViewTenant(request): 
    form = TenantSignupForm(request.POST)
    if request.method == 'POST':     
        if form.is_valid(): 
            user = form.save()
            return redirect('home')


    return render(request,'registration/signup_tenant.html', {'form':form})

def SignUpViewLandlord(request): 
    form = LandlordSignupForm(request.POST)
    if request.method == 'POST':     
        if form.is_valid(): 
            user = form.save()
            return redirect('home')

    return render(request,'registration/signup_landlord.html', {'form':form})
    

@login_required
def ProfileView(request): 
    user = request.user

    if user.is_tenant: 
        return redirect('tenantProfile')

    
    return redirect('landlordProfile')

@login_required
def LandlordProfileView(request): 

    return render(request,'landlord/landlord_profile.html',{'user':request.user})

@login_required
def TenantProfileView(request): 

    return render(request,'tenant/tenant_profile.html',{'user':request.user})
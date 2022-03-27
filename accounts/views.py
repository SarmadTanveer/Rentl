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
    return render(request,'tenant/tenant_profile.html')
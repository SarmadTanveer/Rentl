from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Listing

class PropertyListView(LoginRequiredMixin, ListView):
    model = Listing
    context_object_name = 'listings'
    
    template_name = 'property/my_listings.html'

    def get_queryset(self):
        query = None
        if self.request.user.is_landlord:
            query = Listing.objects.filter(owner = self.request.user) 
        else: 
            query = Listing.objects.filter(is_active = True)
        return query 

class PropertyDetailView(LoginRequiredMixin,DetailView): # new
    model = Listing
    template_name = 'property/listing_detail.html' 

class PropertyCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView): # new
    model = Listing
    template_name = 'property/listing_new.html'
    permission_required = ('propertyManagement.can_create')
    fields = ['title', 'address', 'city', 'state', 'zipcode', 'description', 
    'price', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'main_photo',
     'photo1', 'photo2', 'photo3','photo4', 'photo5', 
    'photo6', 'is_published', 'list_data' ] 

    def form_valid(self,form): 
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PropertyUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView): # new
    model = Listing
    template_name = 'property/listing_edit.html'
    permission_required = ('propertyManagement.can_edit')
    fields = ['title', 'address', 'city', 'state', 'zipcode', 'description', 
    'price', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'main_photo',
     'photo1', 'photo2', 'photo3','photo4', 'photo5', 
    'photo6', 'is_published', 'is_active','list_data' ] 

class PropertyDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView): # new
    model = Listing
    template_name = 'property/listing_delete.html'
    permission_required = ('propertyManagement.can_delete')
    success_url = reverse_lazy('listings')

def CreateLeaseView(request): 
    return render(request,template_name='propertymanagment/create_lease.html' )
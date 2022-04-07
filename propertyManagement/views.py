from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Listing

class PropertyListView(LoginRequiredMixin, ListView):
    model = Listing
    context_object_name = 'listings'
    
    template_name = 'property/my_listings.html'

    def get_queryset(self):
        return Listing.objects.filter(owner = self.request.user)

class PropertyDetailView(LoginRequiredMixin,DetailView): # new
    model = Listing
    template_name = 'property/listing_detail.html' 

class PropertyCreateView(LoginRequiredMixin,CreateView): # new
    model = Listing
    template_name = 'property/listing_new.html'
    fields = ['title', 'address', 'city', 'state', 'zipcode', 'description', 
    'price', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'main_photo',
     'photo1', 'photo2', 'photo3','photo4', 'photo5', 
    'photo6', 'is_published', 'list_data' ] 

    def form_valid(self,form): 
        form.instance.user = self.request.user
        return super().form_valid(form)

class PropertyUpdateView(LoginRequiredMixin,UpdateView): # new
    model = Listing
    template_name = 'property/listing_edit.html'
    fields = ['title', 'address', 'city', 'state', 'zipcode', 'description', 
    'price', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'main_photo',
     'photo1', 'photo2', 'photo3','photo4', 'photo5', 
    'photo6', 'is_published', 'list_data' ] 

class PropertyDeleteView(LoginRequiredMixin,DeleteView): # new
    model = Listing
    template_name = 'property/listing_delete.html'
    success_url = reverse_lazy('listings')
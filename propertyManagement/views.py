from django.views.generic import ListView, DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Listing

class PropertyListView(ListView):
    model = Listing
    template_name = 'home.html'

class PropertyDetailView(DetailView): # new
    model = Listing
    template_name = 'listing_detail.html' 

class PropertyCreateView(CreateView): # new
    model = Listing
    template_name = 'listing_new.html'
    fields = ['title', 'address', 'city', 'state', 'zipcode', 'description', 
    'price', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'main_photo',
     'photo1', 'photo2', 'photo3','photo4', 'photo5', 
    'photo6', 'is_published', 'list_data' ] 

class PropertyUpdateView(UpdateView): # new
    model = Listing
    template_name = 'listing_edit.html'
    fields = ['title', 'address', 'city', 'state', 'zipcode', 'description', 
    'price', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'main_photo',
     'photo1', 'photo2', 'photo3','photo4', 'photo5', 
    'photo6', 'is_published', 'list_data' ] 

class PropertyDeleteView(DeleteView): # new
    model = Listing
    template_name = 'listing_delete.html'
    success_url = reverse_lazy('home')
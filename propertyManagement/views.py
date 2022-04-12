from pyexpat import model
from re import template
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .options import price_choices, bedroom_choices, state_choices
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from .models import Listing, Lease

class PropertyListView(LoginRequiredMixin, ListView):
    model = Listing
    context_object_name = 'listings'
    
    template_name = 'property/my_listings.html'

    def get_queryset(self):
        query = None
        if self.request.user.is_landlord:
            query = Listing.objects.filter(owner = self.request.user) 
        else: 
            query = Listing.objects.filter(List = True)
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
    'photo6', 'List', 'list_data' ] 

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
    'photo6', 'List', 'is_active','list_data' ] 

    
class PropertyDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView): # new
    model = Listing
    template_name = 'property/listing_delete.html'
    permission_required = ('propertyManagement.can_delete')
    success_url = reverse_lazy('listings')

class CreateLeaseView(LoginRequiredMixin,CreateView): 
    model = Lease
    template_name = 'property/create_lease.html'
    success_url = reverse_lazy('landlordProfile')
    fields = ['Listing','tenantFirstName', 'tenantLastName','tenantPicture','lease', 'otherdocument1','otherdocument2','otherdocument3']
    
class PropertyGenView( ListView):
    model = Listing
    context_object_name = 'generallistings'
    
    template_name = 'property/listings.html'
    

class DeleteLeaseView(LoginRequiredMixin, DeleteView): 
    model = Lease
    template_name = 'property/delete_lease.html'
    success_url = reverse_lazy('landlordProfile')

class LeaseDetailView(LoginRequiredMixin,DetailView): 
    model = Lease
    template_name = 'property/lease_detail.html'

class LeaseListView(LoginRequiredMixin,ListView): 
    model = Lease
    template_name = 'property/lease_list.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        listings = Listing.objects.filter(owner = self.request.user)
        leases = Lease.objects.filter(Listing__in = listings)
        context['leases'] = leases
        return context


def search(request):
    queryset_list=Listing.objects.order_by('-list_data')

    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains = keywords)
        
   #City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list=queryset_list.filter(city__iexact = city)

     #State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list=queryset_list.filter(city__iexact = state)
    
    
     # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list=queryset_list.filter(bedrooms__lte=bedrooms)
        
     # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list=queryset_list.filter(price__lte=price)
                
    context={
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'listings':queryset_list,
        'values':request.GET,
    }

    return render(request, 'property/search.html', context)


from django.views.generic import ListView
from django.shortcuts import render
from propertyManagement.models import Listing

# Create your views here.
def HomePageView(request):
    return render(request, 'home.html')

def AboutPageView(request): 
    return render(request, 'about.html')

def ContactPageView(request): 
    return render(request,'contact.html')

class ListingsPageView(ListView): 
    model = Listing
    context_object_name = 'listings'
    template_name = 'listings.html'

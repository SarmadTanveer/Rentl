from django.urls import path 
from .views import HomePageView,AboutPageView, ContactPageView, ListingsPageView

urlpatterns = [
    path('', HomePageView, name='home'),
    path('about/', AboutPageView, name='about'), 
    path('contact/',ContactPageView, name='contact'), 
    path('viewlistings/',ListingsPageView.as_view(), name='allListings')

]
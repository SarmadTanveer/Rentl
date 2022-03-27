from django.urls import path 
from .views import HomePageView,AboutPageView, ContactPageView

urlpatterns = [
    path('', HomePageView, name='home'),
    path('about/', AboutPageView, name='about'), 
    path('contact/',ContactPageView, name='contact'), 

]
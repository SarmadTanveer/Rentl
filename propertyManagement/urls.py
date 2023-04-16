from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
PropertyListView, 
PropertyDetailView, 
PropertyCreateView, 
PropertyUpdateView,
PropertyDeleteView,
CreateLeaseView, 
DeleteLeaseView, 
LeaseDetailView, 
LeaseListView
)

urlpatterns = [
    path('listing/<int:pk>/delete/', PropertyDeleteView.as_view(), name='listing_delete'),
    path('listing/<int:pk>/edit/', PropertyUpdateView.as_view(), name='listing_edit'),
    path('listing/new/', PropertyCreateView.as_view(), name = 'listing_new'),
    path('listing/<int:pk>/', PropertyDetailView.as_view(), name='listing_detail'), # new
    path('viewlistings/', PropertyListView.as_view(), name='listings'),
    path('createLease/',CreateLeaseView.as_view(), name='createLease'),
    path('deleteLease/<int:pk>/',DeleteLeaseView.as_view(), name='deleteLease'),
    path('leasedetails/<int:pk>/',LeaseDetailView.as_view(), name='leaseDetail'), 
    path('viewleases/', LeaseListView.as_view(), name='leases')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
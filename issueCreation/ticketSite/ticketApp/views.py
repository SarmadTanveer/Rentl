from django.shortcuts import render
from django.http import HttpResponse
from .models import Ticket

# Create your views here.
def index(request):
    tickets = Ticket.objects.order_by('-created_at')[:5]
    return render(request, 'index.html', {'tickets': tickets})

def ticket_by_id(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    return render(request, 'ticket_by_id.html', {'ticket':ticket})

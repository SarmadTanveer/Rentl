from django import forms 
from .models import Ticket



class IssueCreationForm(forms.Form): 

    class Meta:
        model = Ticket
        fields = ('title', 'description')

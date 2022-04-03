from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import IssueCreationForm
from .models import Ticket
#from accounts import User


# Create your views here.

# @login_required
# def CreateIssueView(request):
#     form = IssueCreationForm(request.POST)
#     user = request.user
#     property = None 
#     if user.is_tenant: 
#         #get tenant profile from database
#         #get property associated with tenant 
#     else: 
#         #get a list of landlords properties 
#         #show which property to include  

#     if request.method == 'POST': 
#         if form.is_valid():
#             issue = form.save()
#             ##somehow include issue id in this url 
#             return redirect('issueDetail')
#         ##create issue 

#     return render(request, 'issues/create_issue.html', {'form':form})

# @login_required
# def IssueDetailView(request): 
#     #get id from url
#     #pull issue from data base
#     issue = 0 
#     #return issue to template 
#     return render(request,'issues/issue_detail.html', {'issue':issue} )
from django.shortcuts import render

# Create your views here.
def HomePageView(request):
    return render(request, 'home.html')

def AboutPageView(request): 
    return render(request, 'about.html')

def ContactPageView(request): 
    return render(request,'contact.html')
from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    #products = Product.objects.all()
    #return render(request, 'frontend/index.html', {'products': products})
    return render(request, 'frontend/about.html')

def about(request):
    return render(request, 'frontend/about.html')

def contact(request):
    return render(request, 'frontend/contact.html')
    
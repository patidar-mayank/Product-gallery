from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

def product_list(request):
    products=Product.objects.all()
    return render(request,'index.html',{'products':products})


def home(request):
    return HttpResponse('hey guys')
# Create your views here.

from django.shortcuts import render,redirect
from adminpanel.models import Products

def home(request):
    products = Products.objects.all()
    return render(request,'home.html',{'products':products})
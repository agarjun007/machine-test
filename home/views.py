from django.shortcuts import render,redirect
from adminpanel.models import Products
import json

def home(request):
    products = Products.objects.all()
    return render(request,'home.html',{'products':products})

cart_list = []
def add_cart(request,id):
    response = redirect('/')
    cart_list.append(id)
    cart = json.dumps(cart_list)
    response.set_cookie('product_ids',cart)    
    return response

def cart(request):
    product_ids = request.COOKIES.get('product_ids') 
    print('product idss',product_ids)
    product_ids=json.loads(product_ids)
    products=[]
    for id in product_ids: 
        product = Products.objects.get(id=id)
        products.append(product)
    return render(request,'cart.html',{'products':products})

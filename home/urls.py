from django.urls import path
from .views import home,add_cart,cart
urlpatterns=[
    path('',home,name='home'),
    path('add_cart<int:id>/',add_cart,name='add_cart'),
    path('cart/',cart,name='cart')
]
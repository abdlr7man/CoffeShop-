from django.shortcuts import render
from Menu.models import Product 
from Shopping_Cart.models import Cart

def home_page(request):
     products = Product.objects.all()
     cart = Cart.objects.all().first()
     print("here", cart.products)
     return render(request, "index.html", {"products": products})
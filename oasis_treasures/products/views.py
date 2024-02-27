from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    Flower, 
    Product,
    Basket,
    Entourage,
    Package,
    Houseplant
)
from info.models import Branch
from orders.models import Order
from gifts.models import Gift


def home(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "products/home.html", context)
    
def flower_api_view(request):
    flowers = Flower.objects.all()
    context = {
        "flowers": flowers
    }
    return render(request, "products/flowers.html", context)


def product_api_view(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "products/products.html", context)

def basket_api_view(request):
    baskets = Basket.objects.all()
    context = {
        "bascets": baskets
    }
    return render(request, "products/baskets.html", context)

def entourage_api_view(request):
    entourages = (Entourage.objects.all())
    context = {
        "entourages": entourages
    }
    return render(request, "products/entourages.html", context)

def branch_api_view(request):
    branches = Branch.objects.all()
    context = {
        "branches": branches
    }
    return render(request, "products/branches.html", context)

def package_api_view(request):
    packages = Package.objects.all()
    context = {
        "packages": packages
    }
    return render(request, "products/packages.html", context)

def houseplant_api_view(request):
    houseplants = Houseplant.objects.all()
    context = {
        "houseplants": houseplants
    }
    return render(request, "products/houseplants.html", context)

def order_api_view(request):
    orders = Order.objects.all()
    context = {
        "orders": orders
    }
    return render(request, "products/orders.html", context)

def gift_api_view(request):
    gifts = Gift.objects.all()
    context = {
        "gifts": gifts
    }
    return render(request, "products/gifts.html", context)

def send_email_views(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            name,#title
            message, #message
            settings.EMAIL_HOST_USER, #sender if not available considered the default or configered.
            [email, 'kadimovhuseyn35@gmail.com','feridehedov1@gmail.com']
        )
    # message = "spam"
    # email = "quliyev-elcin00@mail.ru"
    # name = "uyyy bimbim"
    # send_mail(
    #     name,#title
    #     message, #message
    #     settings.EMAIL_HOST_USER, #sender if not available considered the default or configered.
    #     [email, 'kadimovhuseyn35@gmail.com','feridehedov1@gmail.com']
    # )
    
    # if request.method == 'POST':
    #     message = request.POST['message']
    #     email = request.POST['email']
    #     name = request.POST['name']
    #     if message and email and name:
    #         send_mail(
    #             name,#title
    #             message, #message
    #             settings.EMAIL_HOST_USER, #sender if not available considered the default or configered.
    #             [email, 'kadimovhuseyn35@gmail.com','feridehedov1@gmail.com']
    #         )
    #     else:
    #         return Http404("voyvoyvoyvoy")
    return render(request, 'products/index.html')
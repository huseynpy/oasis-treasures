import random

from products.models import Product, Flower


def get_random_price():
    prices = random.randint(5, 15)
    return prices

def get_random_description():
    description = "Tərkib: Rəngarəng Gul buketi"
    return description

def get_random_view():
    views = random.randint(50, 150)
    return views

def get_random_code():
    code = random.randint(1, 15)
    return f"00{code}"

def generate_flower_objects():
    flowers = Flower.objects.all()
    bouquet = random.choice(flowers)
    return bouquet

def generate_product_object(amount):
    for _ in range(amount):
        Product.objects.create(
            flower=generate_flower_objects(),
            views_count=get_random_view(),
            description=get_random_description(),
            code=get_random_code(),
            price=get_random_price()
        )
import random

from products.models import Entourage


def get_random_name():
    names = Entourage.objects.all()
    return random.choice(names)

def get_random_price():
    prices = random.randint(7, 15)
    return prices

def get_random_stock_amount():
    stock_amount = random.randint(50, 100)
    return stock_amount


def generate_entourage_objects(amount):
    for _ in range(amount):
        Entourage.objects.create(
             name=get_random_name(),
             price=get_random_price(),
             stock_amount=get_random_stock_amount(),
             is_main=True

        )
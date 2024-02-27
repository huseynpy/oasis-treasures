import random 
from products.models import Flower


def get_random_name():
    names = Flower.objects.all()
    return random.choice(names)

def get_random_price():
    prices = random.randint(5, 15)
    return prices

def get_random_stock_amount():
    stock_amount = random.randint(50, 999)
    return stock_amount


def get_random_code():
    code = random.randint(1, 15)
    return f"00{code}"

def generate_flower_objects(amount):
    for _ in range(amount):
        Flower.objects.create(
             name=get_random_name(),
             price=get_random_price(),
             stock_amount=get_random_stock_amount(),
             is_main=True,
             code=get_random_code()

        )
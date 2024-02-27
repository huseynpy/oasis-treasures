from django.contrib import admin
from .models import (
    Package,
    Product,
    Flower,
    Entourage,
    Houseplant
)

admin.site.register(Package)
admin.site.register(Product)
admin.site.register(Flower)
admin.site.register(Entourage)
admin.site.register(Houseplant)
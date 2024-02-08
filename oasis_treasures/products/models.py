from django.db import models

#
class Product(models.Model):
    pass


class Flower(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField(default=0)
    stock_amount = models.PositiveIntegerField(default=0)
    is_main = models.BooleanField(default=False)
    code = models.PositiveSmallIntegerField(default=0)
    
    def __str__(self) -> str:
        return f"{self.name}"
    
class Houseplant(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField(default=0)
    stock_amount = models.PositiveIntegerField(default=0)
    is_main = models.BooleanField(default=False)
    code = models.PositiveSmallIntegerField(default=0)
    
    def __str__(self) -> str:
        return f"{self.name}"
    
class Entourage(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField(default=0)    
    stock_amount = models.PositiveIntegerField(default=0)
    is_main = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.name}" 
    
class Package(models.Model):
    type_name = models.CharField(max_length=32)
    descriptions = models.CharField(max_length=32)
    price = models.FloatField(default=0)
    
    def __str__(self) -> str:
        return f"{self.type_name}"
    
    
    

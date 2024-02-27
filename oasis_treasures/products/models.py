from django.db import models


class Product(models.Model):
    flower = models.ForeignKey("Flower", on_delete=models.CASCADE)
    views_count = models.PositiveIntegerField(default=0)
    description = models.TextField(max_length=2000)
    code = models.PositiveSmallIntegerField(default=0)
    price = models.FloatField(default=0)

    def __str__(self) -> str:
        return f"Product ({self.flower})"


class Basket(models.Model):
    flower = models.ForeignKey("Flower", on_delete=models.CASCADE)
    entourage = models.ForeignKey("Entourage", on_delete=models.CASCADE)
    package = models.ForeignKey("Package", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Basket {self.pk}"



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
    
    
    

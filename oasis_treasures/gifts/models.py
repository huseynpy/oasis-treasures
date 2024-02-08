from django.db import models


class Gift(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField(default=0)
    code = models.PositiveSmallIntegerField(default=0)
    stock_amount = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(max_length=1024)
    def __str__(self) -> str:
        return f"{self.name}"
    

from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=32)
    map_longtitude = models.CharField(max_length=32)
    map_latitude = models.CharField(max_length=32)
    address = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.name}"
    
    
from django.db import models


# Create your models here.
class BrandModel(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=255)

    def __str__(self):
        return self.brand

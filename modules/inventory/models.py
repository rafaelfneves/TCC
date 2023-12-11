# inventory/models.py
from django.db import models
from modules.material.models import MaterialModel


# Create your models here.
class InventoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    materials = models.CharField(max_length=255)
    weight_grams = models.FloatField()
    fk_materials = models.ForeignKey(MaterialModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.materials} - {self.weight_grams}g"

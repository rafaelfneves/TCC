from django.db import models
from modules.category.models import CategoryModel


# Create your models here.
class MaterialModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    fk_categories = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

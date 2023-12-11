from django.db import models
from modules.user.models import UserModel


# Create your models here.
class VehicleModel(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    plate = models.CharField(max_length=10)
    fk_user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.model} - {self.year} ({self.plate})"

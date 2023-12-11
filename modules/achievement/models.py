from django.db import models
from modules.user.models import UserModel


class AchievementModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    requirement = models.CharField(max_length=255)
    points = models.IntegerField()
    fk_user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.fk_user}"

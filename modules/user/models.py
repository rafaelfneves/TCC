from django.db import models


# Create your models here.
class UserModel(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True)
    role = models.IntegerField(choices=[(0, "Admin"), (1, "User")], default=1)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth_date = models.DateField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    fk_address = models.ForeignKey("Address", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"

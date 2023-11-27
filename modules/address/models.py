from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=50, null=False)
    number = models.IntegerField(null=False)
    complement = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=30, null=False)
    state = models.CharField(max_length=2, null=False)
    zip_code = models.CharField(max_length=9, null=False)

    class Meta:
        unique_together = ["street", "number", "city", "state", "zip_code"]

    def __str__(self):
        return (
            f"{self.street}, {self.number}, {self.city}, {self.state} {self.zip_code}"
        )

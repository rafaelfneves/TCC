import random
import string
from django.db import models


class Voucher(models.Model):
    cod_voucher = models.CharField(max_length=8, primary_key=True)
    hashed_code = models.CharField(max_length=64, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Se o voucher ainda não tem um código, gera um aleatório
        if not self.cod_voucher:
            self.cod_voucher = self.generate_random_code()
        super().save(*args, **kwargs)

    def generate_random_code(self):
        # Gera um código aleatório de 8 caracteres (números e letras)
        characters = string.ascii_letters + string.digits
        return "".join(random.choice(characters) for i in range(8))

    def generate_hash(self):
        # Gere um código de 8 caracteres alfanuméricos aleatórios
        alphanumeric = string.ascii_letters + string.digits
        generated_code = "".join(random.choice(alphanumeric) for _ in range(8))
        return generated_code

    def __str__(self):
        return f"Voucher {self.cod_voucher}"

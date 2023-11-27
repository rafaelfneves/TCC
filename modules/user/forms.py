from django import forms
from .models import UserModel


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel

    fields = [
        "name",
        "surname",
        "cpf",
        "password_hash",
        "role",
        "birth_date",
        "phone",
        "email",
        "fk_address",
    ]

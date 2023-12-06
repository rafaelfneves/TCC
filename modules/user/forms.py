from django import forms
from django.forms import SelectDateWidget
from modules.address.models import AddressModel
from .models import UserModel


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = [
            "name",
            "surname",
            "cpf",
            "role",
            "birth_date",
            "phone",
            "email",
            "password",
            "fk_address",
        ]

        widgets = {
            "birth_date": SelectDateWidget(years=range(1900, 2100)),
        }

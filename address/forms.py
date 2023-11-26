from django import forms
from .models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ("street", "number", "complement", "city", "state", "zip_code")

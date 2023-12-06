from django import forms
from .models import AddressModel


class AddressForm(forms.ModelForm):
    class Meta:
        model = AddressModel
        fields = ["street", "number", "complement", "city", "state", "zip_code"]

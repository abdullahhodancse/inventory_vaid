from django import forms
from app_inv.models.catagory import Catagory


class Catagory_form(forms.ModelForm):
    class Meta:
        model=Catagory
        fields='__all__'

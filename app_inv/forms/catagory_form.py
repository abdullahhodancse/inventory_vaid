from django import forms
from app_inv.models.catagory import Catagory


class catagory(forms.ModelForm):
    class Meta:
        model=Catagory
        fields='__all__'

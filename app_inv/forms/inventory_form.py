from django import forms
from app_inv.models.inventory import inventory
from app_inv.models.catagory import Catagory

class InventoryForm(forms.ModelForm):
    class Meta:
        model = inventory
        exclude = ['user'] 

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  
        super().__init__(*args, **kwargs)

        if user:
            
            self.fields['catagory'].queryset = Catagory.objects.filter(user=user)



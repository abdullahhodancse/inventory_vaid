from django import forms
from app_inv.models.inventory import inventory
from app_inv.models.catagory import Catagory

class InventoryForm(forms.ModelForm):
    class Meta:
        model = inventory
        exclude = ['user']  # user ফিল্ড ফর্মে দেখাবে না

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # view থেকে পাঠানো user নাও
        super().__init__(*args, **kwargs)

        if user:
            # শুধু ওই logged-in user এর category গুলো দেখাবে
            self.fields['catagory'].queryset = Catagory.objects.filter(user=user)



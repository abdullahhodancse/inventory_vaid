from django import forms
from  django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

user=get_user_model()

class loginform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)


    def clean(self):
        cleaned_data=super().clean()
        email=cleaned_data.get('email')
        password=cleaned_data.get('password')
        user=authenticate(email=email,password=password)
        if not user:
            raise forms.ValidationError("Invalid Email or Password")
        self.user = user 

        return cleaned_data
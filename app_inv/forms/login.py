from django import forms
from  django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User=get_user_model()

class loginform(forms.Form):
    email=forms.EmailField()
    pssword=forms.CharField(widget=forms.PasswordInput)


    def clean(self):
        cleaned_data=super().clean()
        email=self.cleaned_data.get('email')
        password=self.cleaned_data.get('password')
        user=authenticate(email=email,password=password)
        if not user:
            raise forms.ValidationError("Invalid Email or Password")

        return cleaned_data
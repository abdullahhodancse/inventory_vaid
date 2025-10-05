from django import forms
from django.contrib.auth import get_user_model

user=get_user_model()

class RegisterForm(forms.Form):
    email=forms.EmailField()
    password1=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(label="confirm password" ,widget=forms.PasswordInput)


    def clean_email(self):
        email=self.cleaned_data.get('email')
        if user.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email
    
    def clean_password(self):
        cleaned=super().clean()
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')
        if  password1 and password2 and password1 != password2:
            raise forms.ValidationError("password does not match")
        return cleaned




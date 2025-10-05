from django.shortcuts import render,redirect
from app_inv.forms.custom_user_forms import RegisterForm
from django.contrib.auth import get_user_model

User=get_user_model()

def register_view(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password1']

            user=User.objects.create_user(email=email,password=password)
            return redirect('login')
    else:
        form = RegisterForm()
            
    return render(request, "register.html", {"form": form})

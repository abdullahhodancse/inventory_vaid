from django.shortcuts import render,redirect
from app_inv.forms.custom_user_forms import RegisterForm
from django.contrib.auth import get_user_model
from app_inv.task import send_verification_email
import uuid

User=get_user_model()

def register_view(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password1']
            ## create inactive user
            user=User.objects.create_user(email=email,password=password,is_active=False)
            token=str(uuid.uuid4())
            #generate UUID
            user.verification_token=token
            user.save()
            # send HTML verification email in background
            send_verification_email.delay(email,token)
            return redirect('login')
    else:
        form = RegisterForm()
            
    return render(request, "register.html", {"form": form})





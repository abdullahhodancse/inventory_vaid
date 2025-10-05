from django.shortcuts import render,redirect
from django.contrib.auth import login
from app_inv.forms.login import loginform


def login_view(request):
    if request.method=='POST':
        form=loginform(request.POST)
        if form.is_valid():
            user=form.changed_data['user']
            login(request,user)
            return redirect('home')
    else:
        form= loginform()
    return render(request,"login.html",{'form':form})





from django.shortcuts import render
from django.contrib.auth import logout

def logout_vi(request):
    logout(request)
    return render(request,'login.html')
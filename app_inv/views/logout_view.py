from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_vi(request):
    logout(request)
    return redirect('home')
from django.shortcuts import render

def complete(request):
    return render(request,'password_reset_complete.html')
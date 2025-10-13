from django.shortcuts import render

def middle(request):
    return render(request,'email_middleware.html')
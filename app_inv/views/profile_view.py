from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User= get_user_model()

@login_required
def profile(request):
    user=request.user
    return render(request, 'profile.html', {'user': user})

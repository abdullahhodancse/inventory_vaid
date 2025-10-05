from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

User = get_user_model()

@login_required
def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # keep user logged in
            return redirect('profile')
        
    else:
        form = PasswordChangeForm(request.user)
        
    return render(request, 'password_change.html', {'form': form})

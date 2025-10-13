from django.shortcuts import redirect
from django.urls import reverse

class EmailVerificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
       
        if request.path.startswith('/admin/'):
            return self.get_response(request)

        allowed_paths = [
            reverse('login'),
            reverse('register'),
            reverse('email_verification'), 
              reverse('logout'),  
        ]

        if request.user.is_authenticated:
            if not getattr(request.user, 'is_verified', True):  
                if not any(request.path.startswith(path) for path in allowed_paths):
                    return redirect(reverse('email_verification'))

        response = self.get_response(request)
        return response

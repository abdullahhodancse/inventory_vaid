from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from django.conf import settings
from app_inv.task.task_paa_reset import send_password_reset_email # fixed import

User = get_user_model()

class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        users = list(form.get_users(email))

        if not users:
            return super().form_valid(form)

        user = users[0]
        current_site = get_current_site(self.request)

        # build reset link manually
        uid = user.pk
        token = self.token_generator.make_token(user)
        protocol = 'https' if self.request.is_secure() else 'http'
        reset_link = f"{protocol}://{current_site.domain}/app/reset/{uid}/{token}/"

        # Send email via Celery
        send_password_reset_email.delay(user.email, reset_link)

        return super().form_valid(form)

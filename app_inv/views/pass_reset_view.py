from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from django.conf import settings

from app_inv.task.task_paa_reset import send_password_reset_email

User = get_user_model()

class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')
    # subject_template_name = 'password_reset_subject.txt'  # এটা আর লাগবে না

    def form_valid(self, form):
        email = form.cleaned_data['email']

        users = list(form.get_users(email))
        if not users:
            return super().form_valid(form)

        user = users[0]

        # Build context for email template
        current_site = get_current_site(self.request)
        context = {
            'email': user.email,
            'domain': current_site.domain,
            'site_name': current_site.name,
            'uid': user.pk,
            'user': user,
            'token': self.token_generator.make_token(user),
            'protocol': 'https' if self.request.is_secure() else 'http',
        }

        # Render HTML email only
        html_message = render_to_string(self.email_template_name, context)
        subject = "Password Reset for MyApp"  # Directly subject string

        # Send email via Celery
        send_password_reset_email.delay(
        subject,
        html_message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email]
    )

        return super().form_valid(form)

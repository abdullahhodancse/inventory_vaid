from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

@shared_task
def send_verification_email(email, token):
    subject = "Verify Your Email"
    verification_link = f"http://127.0.0.1:8000/verify/{token}/"
    
    # Render HTML template
    html_content = render_to_string("verification_email.html", {"verification_link": verification_link})

    # Create email
    msg = EmailMultiAlternatives(
        subject=subject,
        body="Please verify your email",  # fallback text
        from_email=settings.EMAIL_HOST_USER,
        to=[email]
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()



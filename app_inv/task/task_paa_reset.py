from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


@shared_task
def send_password_reset_email(email, reset_link):
    """
    Send a password reset email using Celery.
    Sends both plain text and HTML versions.
    """

    subject = "Reset Your Password"

    # Render HTML email template
    html_content = render_to_string("password_reset_email.html", {
        "reset_link": reset_link
    })

    # Create email
    msg = EmailMultiAlternatives(
        subject=subject,
        body="Please click the link below to reset your password.",  # fallback text
        from_email=settings.EMAIL_HOST_USER,
        to=[email],
    )

    # Attach HTML content
    msg.attach_alternative(html_content, "text/html")

    # Send the email
    msg.send()

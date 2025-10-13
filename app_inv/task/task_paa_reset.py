# app_inv/task/task_pass_reset.py
from celery import shared_task
from django.core.mail import EmailMultiAlternatives

@shared_task
def send_password_reset_email(subject, html_message, from_email, recipient_list):
    """
    Send a password reset email using Celery.
    Only HTML message is used; plain text is optional.
    """
    # Create email
    msg = EmailMultiAlternatives(
        subject=subject,
        body='',  # plain text empty
        from_email=from_email,
        to=recipient_list
    )

    # Attach HTML version
    if html_message:
        msg.attach_alternative(html_message, "text/html")
    
    # Send email
    msg.send()
    return True

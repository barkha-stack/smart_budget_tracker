"""
All alert-related logic lives here
"""

from django.core.mail import send_mail
from django.conf import settings

try:
    from twilio.rest import Client
except ImportError:
    Client = None


def send_budget_email(user, category, spent_percent):
    """
    Sends email alert when budget crosses threshold
    """

    subject = f"⚠ Budget Alert: {category} at {spent_percent}%"

    message = f"""
Hi {user.username},

You have used {spent_percent}% of your budget for "{category}".

Please manage your expenses carefully.

– Smart Budget Tracker
"""

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=True,
    )


def send_sms_alert(phone_number, category, spent_percent):
    if not Client:
        return

    client = Client(
        settings.TWILIO_ACCOUNT_SID,
        settings.TWILIO_AUTH_TOKEN
    )

    client.messages.create(
        body=f"Alert: {spent_percent}% of {category} budget used.",
        from_=settings.TWILIO_PHONE_NUMBER,
        to=phone_number
    )


def send_whatsapp_alert(phone_number, category, spent_percent):
    if not Client:
        return

    client = Client(
        settings.TWILIO_ACCOUNT_SID,
        settings.TWILIO_AUTH_TOKEN
    )

    client.messages.create(
        body=f"⚠ Budget Alert!\n{spent_percent}% spent on {category}",
        from_="whatsapp:+14155238886",
        to=f"whatsapp:{phone_number}"
    )

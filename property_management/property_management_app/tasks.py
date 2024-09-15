from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_rent_due_reminder(tenant_email):
    subject = 'Rent Due Reminder'
    message = 'Your rent is due soon. Please make the payment.'
    from_email = 'no-reply@propertymanagement.com'
    send_mail(subject, message, from_email, [tenant_email])

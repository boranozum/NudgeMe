from django.core.mail import send_mail

def send_email(recipient_email, subject, message):
    # TODO: Handle this with notification tasks
    return send_mail(
        subject,
        message,
        None,
        [recipient_email],
        fail_silently=True,
    )

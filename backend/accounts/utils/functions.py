import random

from accounts.models import UserVerification


def generate_verification_token(user):
    verification_token = ''.join(random.choices('0123456789', k=6))
    UserVerification.objects.create(
        user=user,
        token=verification_token
    )

    return verification_token
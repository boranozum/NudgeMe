import random
import socket

from accounts.models import UserVerification, LoginAttempt


def generate_verification_token(user):
    """
    Generates a 6-digit verification token, temporarily associates with the user and returns the token.

    :param user: User instance
    :return: 6-digit verification token
    """
    verification_token = ''.join(random.choices('0123456789', k=6))
    UserVerification.objects.create(
        user=user,
        token=verification_token
    )

    return verification_token


def log_login_attempt(request, is_successful):
    LoginAttempt.objects.create(
        server_hostname=socket.gethostname(),
        user=request.user,
        remote_address=request.META.get("HTTP_X_REAL_IP"),
        status=LoginAttempt.Status.SUCCESS if is_successful else LoginAttempt.Status.FAIL
    )

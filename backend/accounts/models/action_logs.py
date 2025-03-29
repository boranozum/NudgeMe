from django.db import models
from django.utils import timezone


class ActionLog(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.PROTECT, null=True)
    remote_address = models.CharField(max_length=15, null=True)
    server_hostname = models.CharField(max_length=100, null=True)
    action_dt = models.DateTimeField(default=timezone.now)
    action = models.CharField(max_length=128, null=True)
    view = models.CharField(max_length=100, null=True)
    is_successful = models.BooleanField(default=True)
    error_message = models.TextField(null=True)
    session_token = models.CharField(max_length=100, null=True)
    request_payload = models.CharField(max_length=100, null=True)
    request_kwargs = models.CharField(max_length=100, null=True)
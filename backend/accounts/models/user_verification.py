import datetime

from django.db import models
from django.utils import timezone


class UserVerification(models.Model):
    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE)
    token = models.CharField(max_length=6)
    expires_at = models.DateTimeField()

    @property
    def is_expired(self):
        return self.expires_at < timezone.now()

    def save(self, *args, **kwargs):
        self.expires_at = timezone.now() + datetime.timedelta(minutes=5)
        return super(UserVerification, self).save(*args, **kwargs)
from django.db import models
from django.utils.translation import gettext_lazy as _


class LoginAttempt(models.Model):
    class Status(models.TextChoices):
        FAIL = "FAIL", _("Failed Attempt")
        SUCCESS = "SUCCESS", _("Successful Login")

    user = models.ForeignKey("accounts.User", on_delete=models.DO_NOTHING, verbose_name=_("User"), null=True)
    remote_address = models.GenericIPAddressField("IP Address", null=True)
    server_hostname = models.CharField(max_length=100, null=True)
    status = models.CharField(_("Status"), max_length=10, choices=Status.choices)
    attempt_dt = models.DateTimeField(_("Attempt Time"), auto_now_add=True, db_index=True)
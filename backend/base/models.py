from django.db import models


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='%(class)s_created_by', null=True)
    updated_by = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='%(class)s_updated_by', null=True)

    class Meta:
        abstract = True


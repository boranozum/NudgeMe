from django.db import models

from base.models import AbstractBaseModel
from events.utils.constants import TimeUnitChoices


class EventCategory(AbstractBaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Event(AbstractBaseModel):
    class EventStatus(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(choices=EventStatus, max_length=20, default=EventStatus.ACTIVE)
    snoozed = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    start_dt = models.DateTimeField()
    end_dt = models.DateTimeField(null=True)
    is_recurring = models.BooleanField(default=False)
    frequency = models.IntegerField(null=True)
    frequency_unit = models.CharField(choices=TimeUnitChoices, max_length=10, null=True)

    #FKs
    event_category = models.ForeignKey(EventCategory, on_delete=models.DO_NOTHING, null=True)
    event_type = models.ForeignKey("events.EventType", on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    @property
    def is_deleted(self):
        return self.deleted_at is not None




from django.db import models

from base.models import AbstractBaseModel


class EventType(AbstractBaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    start_dt_required = models.BooleanField(default=False)
    end_dt_required = models.BooleanField(default=False)
    is_all_day_event = models.BooleanField(default=False)

    def __str__(self):
        return self.name
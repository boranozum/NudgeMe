from django.db import models

from events.utils.constants import TimeUnitChoices


class EventDate(models.Model):
    start_dt = models.DateTimeField()
    end_dt = models.DateTimeField(null=True)
    is_recurring = models.BooleanField(default=False)
    frequency = models.IntegerField(null=True)
    frequency_unit = models.CharField(choices=TimeUnitChoices, max_length=10, null=True)

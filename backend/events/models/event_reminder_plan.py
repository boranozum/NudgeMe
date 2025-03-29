from django.db import models

from events.utils.constants import TimeUnitChoices


class EventReminderPlan(models.Model):
    last_n_time_unit = models.CharField(choices=TimeUnitChoices, max_length=10)
    last_n_time_period = models.IntegerField(null=True)
    frequency_time_unit = models.CharField(choices=TimeUnitChoices, max_length=10)
    frequency_time_period = models.IntegerField(null=True)
    is_single_reminder = models.BooleanField(default=False)

    #Fks
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)

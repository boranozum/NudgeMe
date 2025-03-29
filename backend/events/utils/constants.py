from django.db import models


class TimeUnitChoices(models.TextChoices):
    HOURS = 'hours'
    MINUTES = 'minutes'
    SECONDS = 'seconds'
    WEEKS = 'weeks'
    MONTHS = 'months'
    YEARS = 'years'
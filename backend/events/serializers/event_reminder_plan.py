from rest_framework.serializers import ModelSerializer

from events.models import EventReminderPlan
from events.serializers.event import EventSerializer


class EventReminderPlanSerializer(ModelSerializer):
    event = EventSerializer(brief=True)

    class Meta:
        model = EventReminderPlan
        fields = [
            "id",
            "last_n_time_unit",
            "last_n_time_period",
            "frequency_time_unit",
            "frequency_time_period",
            "is_single_reminder",
            "event",
        ]
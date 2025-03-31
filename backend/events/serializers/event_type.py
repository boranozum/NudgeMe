from base.serializers import BaseModelSerializer
from events.models import EventType


class EventTypeSerializer(BaseModelSerializer):
    class Meta:
        model = EventType
        fields = [
            "id",
            "name",
            "description",
            "start_dt_required",
            "end_dt_required",
            "is_all_day_event"
        ]
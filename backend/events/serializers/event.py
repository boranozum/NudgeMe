from rest_framework.relations import PrimaryKeyRelatedField

from base.serializers import BaseModelSerializer
from events.models import Event, EventCategory, EventType
from events.serializers.event_type import EventTypeSerializer


class EventCategorySerializer(BaseModelSerializer):
    class Meta:
        model = EventCategory
        fields = '__all__'
        brief_fields = ["id", "title"]


class EventSerializer(BaseModelSerializer):
    event_category = EventCategorySerializer(brief=True, read_only=True)
    event_type = EventTypeSerializer(required=False)

    event_category_id = PrimaryKeyRelatedField(
        queryset=EventCategory.objects.all(),
        write_only=True,
    )
    event_type_id = PrimaryKeyRelatedField(
        queryset=EventType.objects.all(),
        write_only=True,
    )

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "status",
            "snoozed",
            "deleted_at",
            "event_type",
            "event_type_id",
            "event_category",
            "event_category_id",
            "created_by",
            "updated_by",
            "created_at",
            "updated_at",
            "is_deleted",
            "start_dt",
            "end_dt",
            "is_recurring",
            "frequency",
            "frequency_unit",
        ]
        brief_fields = ["id", "title", "status"]
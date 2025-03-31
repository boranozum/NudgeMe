from base.permissions import ReadOnlyPermission
from base.views import BaseViewSet
from events.models import EventType
from events.serializers.event_type import EventTypeSerializer


class EventTypeViewSet(BaseViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
    permission_classes = (ReadOnlyPermission,)
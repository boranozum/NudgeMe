from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin

from base.mixins import MultiActionMixin
from base.views import BaseViewSet
from events.models import Event, EventCategory
from events.serializers.event import EventSerializer, EventCategorySerializer


class EventCategoryViewSet(
    MultiActionMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    BaseViewSet
):
    serializer_class = EventCategorySerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return EventCategory.objects.all()

        return EventCategory.objects.filter(created_by=self.request.user)


class EventViewSet(
    MultiActionMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    BaseViewSet
):
    serializer_class = EventSerializer
    ordering = ("created_at",)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Event.objects.all()

        return Event.objects.filter(created_by=self.request.user)

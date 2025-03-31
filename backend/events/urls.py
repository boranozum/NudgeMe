from rest_framework import routers

from events.views.event import EventViewSet, EventCategoryViewSet
from events.views.event_type import EventTypeViewSet

router = routers.SimpleRouter()

router.register("types", EventTypeViewSet, basename='event-types')
router.register("categories", EventCategoryViewSet, basename='event-categories')
router.register("", EventViewSet, basename='events')

urlpatterns = router.urls
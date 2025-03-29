from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from base.mixins import PaginationMixin, RetrieveMixin
from base.permissions import BaseModelPermission


class BaseViewSet(
    PaginationMixin,
    RetrieveMixin,
    ListModelMixin,
    GenericViewSet
):
    permission_classes = (BaseModelPermission,)
    filter_backends = [SearchFilter, OrderingFilter]
    only_superuser = False



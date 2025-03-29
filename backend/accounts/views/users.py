from django.contrib.auth import get_user_model

from accounts.serializers.user import UserSerializer
from base.mixins import MultiActionMixin
from base.views import BaseViewSet

User = get_user_model()

class UserViewSet(
    MultiActionMixin,
    BaseViewSet,
):
    only_superuser = True
    queryset = User.objects.filter(id__gt=0)
    ordering = ['pk']
    serializer_class = UserSerializer

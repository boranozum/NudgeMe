from rest_framework.permissions import BasePermission

from accounts.models import GlobalPermission


def grant_permission_to_user(user, *permission_names):
    user.user_permissions.add(*GlobalPermission.objects.filter(codename__in=permission_names))


class IsAuthenticatedPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_active and request.user.is_authenticated


class BaseModelPermission(IsAuthenticatedPermission):
    def has_permission(self, request, view):
        is_authenticated = super().has_permission(request, view)
        if not is_authenticated:
            return False

        if getattr(view, 'only_superuser', False) and not request.user.is_superuser:
            return False

        if not getattr(view, 'only_superuser', False) and (permission_name := getattr(view, 'permission_name', None)):
            return request.user.has_perm(f"accounts.{permission_name}")

        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        return obj.created_by == request.user


class ReadOnlyPermission(BaseModelPermission):
    def has_permission(self, request, view):
        has_permission = super().has_permission(request, view)
        if not has_permission:
            return False

        if request.user.is_superuser or request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True

        return super().has_object_permission(request, view, obj)

from django.utils.translation import gettext_lazy as _

from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator(BasePermission):
    """
    Разрешение только для модераторов.
    Проверяет, что пользователь авторизован и имеет роль MODERATOR.
    """
    message = _("You are not a moderator.")

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == UserRoles.MODERATOR:
            return True
        return False


class IsSuperuser(BasePermission):
    """
    Разрешение только для суперпользователей.
    Проверяет, что пользователь авторизован и является суперпользователем.
    """
    message = _("You are not a superuser.")

    def has_permission(self, request, view):
        # if request.user.is_authenticated and request.user.role == UserRoles.ADMIN:
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        return False
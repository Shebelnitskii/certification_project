from rest_framework.permissions import BasePermission


class IsOwnerOrModerator(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешить доступ, если пользователь сотрудник (is_staff=True)
        if request.user.is_staff:
            return True

        # Разрешить доступ, если пользователь является самим пользователем
        return request.user == obj

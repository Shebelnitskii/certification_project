from rest_framework.permissions import BasePermission

class IsActiveOwner(BasePermission):
    def has_permission(self, request, view):
        # Проверяем, является ли текущий пользователь активным сотрудником
        return request.user.is_active
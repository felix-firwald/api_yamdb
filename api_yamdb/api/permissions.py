from rest_framework import permissions


class SafeMethodsOnlyPermission(permissions.BasePermission):
    """Права доступа для администратора, супрюзера и при безопасных методах"""

    """def has_permission(self, request, view):
        if (request.user.is_superuser
           or request.method in permissions.SAFE_METHODS):
            return True
        elif request.user.is_authenticated and request.user.is_admin:
            return True"""
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_superuser
            or request.user.is_authenticated and request.user.is_admin
        )


class IsRoleAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return (
            user.is_authenticated and user.is_admin
            or user.is_superuser
        )

    def has_object_permission(self, request, view, obj):
        user = request.user
        return (
            user.is_authenticated and user.is_admin
            or user.is_superuser
        )


class IsRoleModerator(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return (
            user.is_authenticated and user.is_moderator
            or user.is_staff
        )

    def has_object_permission(self, request, view, obj):
        user = request.user
        return (
            user.is_authenticated and user.is_moderator
            or user.is_staff
        )


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return (
            user.is_authenticated and user.is_user
            or request.method in permissions.SAFE_METHODS
        )

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.method in permissions.SAFE_METHODS
        )


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
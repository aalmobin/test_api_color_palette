from rest_framework import permissions


class UpdateOwnColorPalette(permissions.BasePermission):
    """Allow User is trying to update their own color palette"""

    def has_object_permission(self, request, view, obj):
        """Check User is trying to Update their own color palette"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user.id == request.user.id

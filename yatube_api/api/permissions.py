from rest_framework import permissions


class AuhorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method != 'GET' or request.method != 'POST':
            return True

    def has_object_permission(self, request, view, obj):
        if (request.method in permissions.SAFE_METHODS
                or obj.author == request.user):
            return True

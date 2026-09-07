from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'


class IsAnalyst(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'analyst'


class IsViewer(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'viewer'


class RecordPermission(BasePermission):
    def has_permission(self, request, view):

        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.role == 'admin':
            return True

        if request.user.role in ['analyst', 'viewer']:
            return request.method in SAFE_METHODS

        return False 
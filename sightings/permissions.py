from rest_framework.permissions import BasePermission

class CanCreateSighting(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['silver', 'golden']

class CanDeleteSighting(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'golden':
            return True
        return obj.created_by_id == request.user.id

class CanConfirmSighting(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['silver', 'golden']
     
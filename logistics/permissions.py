from rest_framework import permissions
from .models import User


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == User.Role.ADMIN

class IsDriver(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == User.Role.DRIVER

class IsShipmentOwnerOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.role == User.Role.ADMIN:
            return True
        return obj.customer == request.user or obj.driver == request.user

    
# from rest_framework import permissions
# from .models import User


# class IsAdmin(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return bool(
#             request.user 
#             and request.user.is_authenticated 
#             and getattr(request.user, 'role', None) == User.Role.ADMIN
#         )


# class IsDriver(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return bool(
#             request.user 
#             and request.user.is_authenticated 
#             and getattr(request.user, 'role', None) == User.Role.DRIVER
#         )


# class IsShipmentOwnerOrAdmin(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_authenticated)

#     def has_object_permission(self, request, view, obj):
#         if getattr(request.user, 'role', None) == User.Role.ADMIN:
#             return True
#         return obj.customer == request.user or obj.driver == request.user
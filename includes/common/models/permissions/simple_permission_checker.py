from rest_framework.permissions import BasePermission

from includes.common.identity_utils import (
    has_any_permission,
)


class SimplePermissionChecker(BasePermission):
    view: list[int] = []
    obj: list[int] = []

    @classmethod
    def set_permissions(cls, view: list[int] = None, obj: list[int] = None):
        if view is None:
            view = []
        if obj is None:
            obj = []
        cls.view = view
        cls.obj = obj
        return cls

    def has_permission(self, request, view):
        if not len(self.view):
            return True
        return has_any_permission(self.view, request)

    def has_object_permission(self, request, view, obj):
        if not len(self.obj):
            return True
        return has_any_permission(self.obj, request)

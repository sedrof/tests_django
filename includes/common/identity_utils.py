import uuid
from typing import TypedDict

from django.db.models import IntegerChoices
from rest_framework.request import Request

from includes.common.models.permissions.bigcommand_user_permissions import (
    PERMISSION_INHERITANCE,
)


class UserType(IntegerChoices):
    Owner = 1
    Subuser = 2
    Staff = 3
    Admin = 4
    BigCommand = 5


class UserIdentity(TypedDict):
    user_type: UserType
    user_id: str
    owner_id: str
    permissions: list[int]
    timezone: str


ALL_STAFF = [UserType.Staff, UserType.Admin, UserType.BigCommand]


def get_owner_id(request: Request) -> uuid.UUID:
    return request.identity["owner_id"]


def get_owner(request: Request):
    if request.user.is_owner or request.user.is_staff:
        return request.user
    return request.user.owner


def get_user_id(request: Request) -> uuid.UUID:
    return request.identity["user_id"]


def get_user_type(request: Request) -> UserType:
    return request.identity["user_type"]


def get_user_permissions(request: Request) -> set[int]:
    return request.identity["permissions"]


def has_all_permissions(permissions: list[int], request: Request) -> bool:
    """
    Checks if the authenticated user has all listed permissions
    """
    if is_staff_or_owner(request):
        return True

    user_permissions = get_user_permissions(request)
    return set(permissions).issubset(user_permissions)


def has_any_permission(permissions: list[int], request: Request) -> bool:
    """
    Checks if the authenticated user has any of the listed permissions either directly
    or inherited.
    """
    inherited_perms = [
        inherited_perm
        for base_perms in permissions
        for inherited_perm in PERMISSION_INHERITANCE.get(base_perms, [])
    ]
    if is_staff_or_owner(request):
        return True
    user_permissions = get_user_permissions(request)
    for perm in permissions + inherited_perms:
        if perm in user_permissions:
            return True
    return False


def is_staff_or_owner(request: Request) -> bool:
    if get_user_type(request) in ALL_STAFF:
        return True

    owner_id = get_owner_id(request)
    user_id = get_user_id(request)
    return owner_id == user_id

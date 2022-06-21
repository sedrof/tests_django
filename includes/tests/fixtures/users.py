import datetime
import uuid
from typing import Union
from uuid import UUID

import jwt

from includes.common.identity_utils import UserType, UserIdentity
from includes.common.secrets_manager import get_environment_secret


def create_test_admin(user_id: Union[str, UUID] = None) -> UserIdentity:
    user_id = user_id or uuid.uuid4()
    return {
        "user_type": UserType.Staff,
        "user_id": str(user_id),
        "owner_id": str(user_id),
        "permissions": [],
        "timezone": "America/Chicago",
    }


def create_test_owner(user_id: Union[str, UUID] = None) -> UserIdentity:
    user_id = user_id or uuid.uuid4()
    return {
        "user_type": UserType.Owner,
        "user_id": str(user_id),
        "owner_id": str(user_id),
        "permissions": [],
        "timezone": "America/Chicago",
    }


def create_test_subuser(
    owner_id: Union[str, UUID], permissions: list[int], user_id: Union[str, UUID] = None
) -> UserIdentity:
    """
    Returns a dummy subuser identity and assigns the given permissions to the subuser.
    """
    user_id = user_id or uuid.uuid4()
    return {
        "user_type": UserType.Subuser,
        "user_id": str(user_id),
        "owner_id": str(owner_id),
        "permissions": permissions,
        "timezone": "America/Chicago",
    }


def authenticate_user(client, identity: UserIdentity):
    """
    Authenticates a user against an instance of DRF's api test client for
    testing authenticated views.
    """
    AUTH_SIGNING_KEY = get_environment_secret("AUTH_SIGNING_KEY")
    exp = datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * 30)
    payload = {
        **identity,
        "iss": "bigcommand_account",
        "aud": "bigcommand_users",
        "exp": exp,
    }
    token = jwt.encode(payload, key=AUTH_SIGNING_KEY, algorithm="RS256")
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")


class TestUsers:
    """
    Mixin class that injects dummy users for testing authenticated views.
    """

    @classmethod
    def setUpTestData(cls):
        cls.admin = create_test_admin()
        cls.owner1 = create_test_owner()
        cls.owner2 = create_test_owner()
        cls.subuser_no_perm = create_test_subuser(
            owner_id=cls.owner1["owner_id"], permissions=[]
        )

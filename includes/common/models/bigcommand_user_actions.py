from typing import List, Type

from django.db import models


class AccountActions(models.IntegerChoices):
    UpdatedAccountInformation = 1
    UpdatedBusinessInformation = 2


class AdiloActions(models.IntegerChoices):
    ...


class BigDriveActions(models.IntegerChoices):
    ...


class BigPartnerActions(models.IntegerChoices):
    ...


class BoomAffiliateActions(models.IntegerChoices):
    ...


class BoomFrontActions(models.IntegerChoices):
    CreateFunnel = 501


class ContactActions(models.IntegerChoices):
    ...


class CorinaActions(models.IntegerChoices):
    ...


class HelpCenterActions(models.IntegerChoices):
    ...


class HomeActions(models.IntegerChoices):
    ...


class HuulaActions(models.IntegerChoices):
    ...


class InboxBirdActions(models.IntegerChoices):
    ...


class PortalActions(models.IntegerChoices):
    ...


class uVendiActions(models.IntegerChoices):
    ...


USER_ACTION_TYPES: List[Type[models.IntegerChoices]] = [
    AccountActions,
    BoomFrontActions,
]

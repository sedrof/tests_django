from django.db import models
from django.utils.translation import gettext_lazy as _
from pydantic import BaseModel, constr

from includes.common.models.uuid_primary_key import UUIDPrimaryKey
from includes.common.validators.schema import validate_schema


def default_phone():
    return {
        "country": "United States",
        "phone": "",
        "isVerified": False,
        "extension": "",
    }


class BaseAddress(UUIDPrimaryKey):
    addressL1 = models.CharField(
        verbose_name=_("address line 1"),
        max_length=200,
        default="",
        blank=True,
        help_text=_("address line 1."),
    )
    addressL2 = models.CharField(
        verbose_name=_("address line 2"),
        max_length=50,
        default="",
        blank=True,
        help_text=_("address line 2 for: unit, apartment, suite number etc."),
    )
    city = models.CharField(
        verbose_name=_("city"),
        max_length=50,
        default="",
        blank=True,
    )
    region = models.CharField(
        verbose_name=_("region"),
        max_length=50,
        default="",
        blank=True,
    )
    zip = models.CharField(
        verbose_name=_("zip"),
        max_length=30,
        default="",
        blank=True,
    )
    country = models.CharField(
        verbose_name=_("country"),
        max_length=30,
        default="",
        blank=True,
    )
    phone = models.JSONField(
        verbose_name=_("phone"),
        help_text=_(
            _(
                "the contacts phone number. It should contain the country and the number."
            )
        ),
        null=True,
        default=default_phone,
    )

    class Meta:
        abstract = True
        default_permissions = []

    def save(self, *args, **kwargs):
        validate_schema(self.phone, PhoneSchema)
        super().save(*args, **kwargs)


class PhoneSchema(BaseModel):
    country: str = None
    phone: str = None
    isVerified: bool = False
    extension: constr(max_length=10) = None

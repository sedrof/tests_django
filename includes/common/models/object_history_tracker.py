from django.db import models
from django.utils.translation import gettext_lazy as _


class ObjectHistoryTracker(models.Model):
    creationDate = models.DateTimeField(
        verbose_name=_("creation date"),
        editable=False,
        auto_now_add=True,
    )
    createdBy = models.UUIDField(
        verbose_name=_("created by"),
        editable=False,
        null=True,
        help_text=_("the Id of the BigCommand account user who added this object."),
    )
    lastModifiedDate = models.DateTimeField(
        verbose_name=_("last modified date"),
        editable=False,
        auto_now=True,
    )
    lastModifiedBy = models.UUIDField(
        verbose_name=_("last modified by"),
        help_text=_(
            "the Id of the BigCommand account user who last modified this object."
        ),
        null=True,
        editable=False,
    )

    class Meta:
        abstract = True

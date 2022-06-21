from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .common import LanguageFields


class Tag(LanguageFields):
    name = models.CharField(
        verbose_name=_("name"),
        max_length=50,
        unique=True,
    )

    class Meta(LanguageFields.Meta):
        verbose_name = _("tag")
        verbose_name_plural = _("tags")
        indexes = [
            models.Index(fields=["name"]),
        ]
        default_permissions = []

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tag-detail", args=[str(self.name)])

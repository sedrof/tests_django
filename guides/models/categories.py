from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from articles.models.common import TitleSlugFields, DescriptionField
from includes.common.bigcommand_apps import BigCommandApps


class Category(TitleSlugFields, DescriptionField):
    thumbnailURL = models.URLField(
        verbose_name=_("thumbnail url"),
        max_length=200,
        blank=True,
        default="",
        help_text=_("optional category thumbnail."),
    )
    app = models.PositiveSmallIntegerField(
        verbose_name=_("app"),
        choices=BigCommandApps.choices,
        null=True,
        help_text=_(
            "the BigCommand app ID this category apply to. Required for relevance filtering."
        ),
    )

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")
        default_permissions = []

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("guide-category-detail", kwargs={"slug":self.slug, "version":"v1"})

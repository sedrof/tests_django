from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from articles.models.common import TitleSlugFields, DescriptionField


class Topic(TitleSlugFields, DescriptionField):
    category = models.ForeignKey(
        verbose_name=_("category"),
        to="Category",
        on_delete=models.SET_NULL,
        null=True,
        related_name="topics",
        related_query_name="topic",
    )

    class Meta:
        verbose_name = _("topic")
        verbose_name_plural = _("topics")
        default_permissions = []

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("guide-topic-detail", kwargs={"slug":self.slug, "version":"v1"})

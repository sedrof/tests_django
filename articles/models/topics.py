from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from articles.models.common import LanguageFields, TitleSlugFields


class Topic(LanguageFields, TitleSlugFields):
    description = models.CharField(
        verbose_name=_("description"),
        max_length=200,
        blank=True,
        default="",
        help_text=_("optional description for this topic."),
    )
    category = models.ForeignKey(
        verbose_name=_("category"),
        to="Category",
        on_delete=models.CASCADE,
        related_name="topics",
        related_query_name="topic",
        help_text=_("the category this topic belongs to."),
    )

    class Meta(LanguageFields.Meta):
        verbose_name = _("topic")
        verbose_name_plural = _("topics")
        default_permissions = []

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("topic-detail", args=[str(self.slug)])

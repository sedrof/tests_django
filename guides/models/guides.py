from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from articles.models.common import TitleSlugFields, DescriptionField, Member
from articles.models.tags import Tag


class Lesson(TitleSlugFields):
    content = models.TextField(
        verbose_name=_("content"), help_text=_("the body content of the post.")
    )
    stepNumber = models.PositiveSmallIntegerField(
        verbose_name=_("step number"),
        help_text=_("lesson step in the guide"),
        validators=[MinValueValidator(1)],
    )
    readDuration = models.DurationField(verbose_name=_("read duration"), null=True)
    watchDuration = models.DurationField(verbose_name=_("watch duration"), null=True)
    videoTranscript = models.TextField(
        verbose_name=_("video transcript"),
        blank=True,
        default="",
        help_text=_("optional video transcript."),
    )
    isHelpFulCount = models.PositiveIntegerField(
        verbose_name=_("is helpful count"),
        default=0,
        help_text=_("how many members found this lesson useful."),
    )
    isNotHelpFulCount = models.PositiveIntegerField(
        _("is not helpful count"),
        default=0,
        help_text=_("how many members did not find this lesson useful."),
    )

    class Meta:
        verbose_name = _("lesson")
        verbose_name_plural = _("lessons")
        ordering = ["stepNumber"]
        indexes = [
            models.Index(fields=["stepNumber"]),
        ]
        default_permissions = []

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("lesson-detail", args=[str(self.slug)])


class Guide(TitleSlugFields, DescriptionField):
    slug = None

    lessons = models.ManyToManyField(
        verbose_name=_("lessons"),
        to=Lesson,
        blank=True,
        related_name="guides",
        related_query_name="guide",
    )
    tags = models.ManyToManyField(
        verbose_name=_("tags"),
        to=Tag,
        blank=True,
        related_name="guides",
        related_query_name="guide",
    )
    topic = models.ForeignKey(
        verbose_name=_("topic"),
        to="Topic",
        on_delete=models.CASCADE,
        related_name="guides",
        related_query_name="guide",
    )
    isPinned = models.BooleanField(
        verbose_name=_("is pinned"),
        default=False,
        help_text=_("pinned feature requests stick to the top."),
    )
    creators = models.ManyToManyField(
        verbose_name=_("creators"),
        to=Member,
        related_name="guides",
        related_query_name="guide",
    )

    class Meta:
        verbose_name = _("guide")
        verbose_name_plural = _("guides")
        default_permissions = []

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("guide-detail", kwargs={"pk": str(self.pk), "version": "v1"})

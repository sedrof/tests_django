from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from articles.models import Tag
from articles.models.common import Comment, TitleSlugFields, Member
from includes.common.bigcommand_apps import BigCommandApps


class FeatureRequest(TitleSlugFields):
    class Phases(models.IntegerChoices):
        UnderReview = 1
        InRoadMap = 2
        BetaRelease = 3
        Launched = 4
        Cancelled = 5

    class CriticalityLevels(models.IntegerChoices):
        NiceToHave = 1
        Important = 2
        Critical = 3

    content = models.TextField(
        verbose_name=_("content"), help_text=_("the body content of the post.")
    )
    featuredImageURL = models.URLField(
        verbose_name=_("featured image url"),
        max_length=200,
        blank=True,
        default="",
        help_text=_("optional featured image url."),
    )
    tags = models.ManyToManyField(
        verbose_name=_("tags"),
        to=Tag,
        blank=True,
        related_name="featureRequests",
        related_query_name="featureRequest",
    )
    publishDate = models.DateTimeField(
        verbose_name=_("publish date"), auto_now_add=True
    )
    lastModifiedDate = models.DateTimeField(
        verbose_name=_("last modified date"), auto_now=True
    )
    level = models.PositiveSmallIntegerField(
        verbose_name=_("criticality level"),
        choices=CriticalityLevels.choices,
        default=CriticalityLevels.Important,
        help_text=_("how critical is this feature."),
    )
    phase = models.PositiveSmallIntegerField(
        verbose_name=_("phase"),
        choices=Phases.choices,
        default=Phases.UnderReview,
        help_text=_("current phase pf this feature request."),
    )
    app = models.PositiveSmallIntegerField(
        verbose_name=_("app"),
        choices=BigCommandApps.choices,
        help_text=_("the bigcommand app ID this feature request applies to."),
    )
    author = models.ForeignKey(
        verbose_name=_("author"),
        to=Member,
        on_delete=models.CASCADE,
        related_name="featureRequests",
        related_query_name="featureRequest",
    )
    isPinned = models.BooleanField(
        verbose_name=_("is pinned"),
        default=False,
        help_text=_("pinned feature requests stick to the top."),
    )
    isPublic = models.BooleanField(
        verbose_name=_("is public"),
        default=False,
        help_text=_("public feature request will show up in public portal."),
    )
    comments = models.ManyToManyField(
        verbose_name=_("comments"),
        to=Comment,
        blank=True,
        related_name="featureRequests",
        related_query_name="featureRequest",
    )

    class Meta:
        verbose_name = _("feature requests")
        verbose_name_plural = _("feature request")
        ordering = ["-publishDate"]
        indexes = [
            models.Index(fields=["level"]),
            models.Index(fields=["phase"]),
            models.Index(fields=["app"]),
            models.Index(fields=["-publishDate"]),
        ]
        default_permissions = []

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("feature-request-detail", args=[str(self.slug)])


class RoadMap(models.Model):
    feature = models.OneToOneField(
        verbose_name=_("feature"),
        to=FeatureRequest,
        on_delete=models.CASCADE,
        limit_choices_to={"phase": FeatureRequest.Phases.InRoadMap},
    )
    devStartDate = models.DateField(verbose_name=_("development start date"), null=True)
    expectedReleaseDate = models.DateField(
        verbose_name=_("expected release date"), null=True
    )
    isPublic = models.BooleanField(
        verbose_name=_("is public"),
        default=False,
        help_text=_("is this roadmap public."),
    )

    class Meta:
        verbose_name = _("roadmap")
        verbose_name_plural = _("roadmaps")
        ordering = ["-devStartDate"]
        indexes = [
            models.Index(fields=["-devStartDate"]),
            models.Index(fields=["-expectedReleaseDate"]),
        ]
        default_permissions = []

    def __str__(self):
        return "Roadmap for '%(feature)s'" % {"feature": self.feature.title}

    def get_absolute_url(self):
        return reverse("road-map-detail", args=[str(self.pk)])


class Vote(models.Model):
    voter = models.ForeignKey(
        verbose_name=_("voter"),
        to=Member,
        on_delete=models.SET_NULL,
        null=True,
        related_name="featureVotes",
        related_query_name="featureVote",
    )
    featureRequest = models.ForeignKey(
        verbose_name=_("feature request"),
        to=FeatureRequest,
        on_delete=models.CASCADE,
        related_name="votes",
        related_query_name="vote",
    )
    date = models.DateTimeField(verbose_name=_("vote date"), auto_now_add=True)

    class Meta:
        verbose_name = _("vote")
        verbose_name_plural = _("votes")
        ordering = ["-date"]
        indexes = [
            models.Index(fields=["-date"]),
        ]
        default_permissions = []

    def __str__(self):
        return "Feature vote for '%(feature)s'" % {"feature": self.featureRequest.title}

    def get_absolute_url(self):
        return reverse("feature-request-vote-detail", args=[str(self.pk)])

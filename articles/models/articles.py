from django.db import models
from django.db.models import QuerySet
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from .common import LanguageFields, Member, TitleSlugFields
from .tags import Tag


class Article(LanguageFields, TitleSlugFields):
    authors = models.ManyToManyField(
        verbose_name=_("author"),
        to=Member,
        related_name="articles",
        related_query_name="article",
        help_text=_("all authors who contributed to this article."),
    )
    tags = models.ManyToManyField(
        verbose_name=_("tags"),
        to=Tag,
        blank=True,
        related_name="articles",
        related_query_name="article",
    )
    content = models.TextField(
        verbose_name=_("content"), help_text=_("the html body content of the article.")
    )
    publishDate = models.DateTimeField(
        verbose_name=_("publish date"), auto_now_add=True
    )
    lastModifiedDate = models.DateTimeField(
        verbose_name=_("last modified date"), auto_now=True
    )
    isHelpFulCount = models.PositiveIntegerField(
        verbose_name=_("is helpful count"),
        default=0,
        editable=False,
        help_text=_("how many viewers found this article helpful."),
    )
    isNotHelpFulCount = models.PositiveIntegerField(
        verbose_name=_("is not helpful count"),
        default=0,
        editable=False,
        help_text=_("how many viewers did not find this article helpful."),
    )
    topic = models.ForeignKey(
        verbose_name=_("topic"),
        to="Topic",
        on_delete=models.SET_NULL,
        null=True,
        related_name="articles",
        related_query_name="article",
        help_text=_("the topic this article belongs to."),
    )

    class Meta(LanguageFields.Meta):
        verbose_name = _("article")
        verbose_name_plural = _("articles")
        default_permissions = []

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"slug":self.slug, "version":"v1"})

    def related_articles(self) -> QuerySet:
        """
        Returns a queryset of 10 other recent articles with similar tags.
        """
        return (
            Article.objects.filter(tags__in=self.tags.all())
            .exclude(pk=self.pk)
            .distinct()[:10]
        )


class ArticleView(models.Model):
    article = models.ForeignKey(
        verbose_name=_("article"),
        to=Article,
        on_delete=models.CASCADE,
        related_name="views",
        related_query_name="view",
    )
    date = models.DateTimeField(
        verbose_name=_("date"),
        auto_now_add=True,
    )
    userId = models.UUIDField(
        verbose_name=_("created by"),
        help_text=_("id of the BigCommand user if authenticated."),
        null=True,
        editable=False,
    )
    ipAddress = models.GenericIPAddressField(
        verbose_name=_("ip address"),
        null=True,
        editable=False,
        help_text=_("client IP address"),
    )

    class Meta:
        verbose_name = _("article view")
        verbose_name_plural = _("article views")
        indexes = [
            models.Index(fields=["date"]),
        ]
        default_permissions = []

    def __str__(self):
        return "View for '%(article)s'" % {"article": self.article.title}

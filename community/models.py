from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from articles.models.common import Comment, Member, TitleSlugFields, DescriptionField
from articles.models.tags import Tag


class Post(TitleSlugFields):
    content = models.TextField(
        verbose_name=_("content"), help_text=_("the html body content of the post.")
    )
    thumbnailURL = models.URLField(
        verbose_name=_("thumbnail url"),
        max_length=200,
        blank=True,
        default="",
        help_text=_("optional post thumbnail url."),
    )
    publishDate = models.DateTimeField(
        verbose_name=_("publish date"), auto_now_add=True
    )
    lastModifiedDate = models.DateTimeField(
        verbose_name=_("last modified date"), auto_now=True
    )
    category = models.ManyToManyField(
        verbose_name=_("category"),
        to="Category",
        help_text=_("the category this post belongs to."),
    )
    author = models.ForeignKey(
        verbose_name=_("author"), to=Member, on_delete=models.SET_NULL, null=True
    )
    allowComments = models.BooleanField(verbose_name=_("allow comments"), default=False)
    tags = models.ManyToManyField(
        verbose_name=_("tags"),
        to=Tag,
        blank=True,
        related_name="communityPosts",
        related_query_name="communityPost",
    )
    isPinned = models.BooleanField(
        verbose_name=_("is pinned"),
        default=False,
        help_text=_("pinned posts stick to the top."),
    )
    comments = models.ManyToManyField(
        verbose_name=_("comments"), to=Comment, blank=True
    )

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")
        ordering = ["-publishDate"]
        indexes = [
            models.Index(fields=["-publishDate"]),
        ]
        default_permissions = []

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "community-post-detail", kwargs={"slug": self.slug, "version": "v1"}
        )


class Category(TitleSlugFields, DescriptionField):
    thumbnailURL = models.URLField(
        verbose_name=_("thumbnail url"),
        max_length=200,
        blank=True,
        default="",
        help_text=_("optional category thumbnail."),
    )

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")
        default_permissions = []

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "community-category-detail", kwargs={"slug": self.slug, "version": "v1"}
        )


class PostView(models.Model):
    post = models.ForeignKey(
        verbose_name=_("post"),
        to=Post,
        on_delete=models.CASCADE,
        related_name="posts",
        related_query_name="post",
    )
    date = models.DateTimeField(verbose_name=_("date"), auto_now_add=True)
    durationOnPage = models.DurationField(verbose_name=_("duration on page"), null=True)
    percentageRead = models.DecimalField(
        verbose_name=_("percentage read"), null=True, max_digits=4, decimal_places=1
    )
    isUnique = models.BooleanField(verbose_name=_("is unique"), default=True)
    ipAddress = models.GenericIPAddressField(
        verbose_name=_("ip address"),
        null=True,
        editable=False,
        help_text=_("client IP address"),
    )

    class Meta:
        verbose_name = _("post view")
        verbose_name_plural = _("post views")
        default_permissions = []

    def __str__(self):
        return "View for '%(post)s'" % {"post": self.post.title}

    def get_absolute_url(self):
        return reverse(
            "community-post-view-detail", kwargs={"pk": str(self.pk), "version": "v1"}
        )

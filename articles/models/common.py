from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from includes.common.supported_languages import SupportedLanguages


class LanguageFields(models.Model):
    language = models.CharField(
        verbose_name=_("language"),
        max_length=10,
        choices=SupportedLanguages.choices,
        default=SupportedLanguages.EN,
        help_text=_("the language this content is in."),
    )
    englishVersion = models.ForeignKey(
        verbose_name=_("english version"),
        to="self",
        on_delete=models.SET_NULL,
        null=True,
        related_name="translations",
        related_query_name="translation",
        limit_choices_to={"language": SupportedLanguages.EN},
        help_text=_(
            """
            references the english version of the content. This enables to 
            find the content translation in a different language.
            """
        ),
    )

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=["language"]),
        ]


class TitleSlugFields(models.Model):
    title = models.CharField(
        verbose_name=_("title"), max_length=150, validators=[MinLengthValidator(2)]
    )
    slug = models.SlugField(
        verbose_name=_("slug"),
        max_length=150,
        allow_unicode=True,
        unique=True,
        editable=False,
        help_text=_("the content slug. Accepts unicode characters."),
    )

    class Meta:
        abstract = True


class DescriptionField(models.Model):
    description = models.CharField(
        verbose_name=_("description"),
        max_length=200,
        blank=True,
        default="",
        help_text=_("optional description for this content."),
    )

    class Meta:
        abstract = True


class Member(models.Model):
    class MemberRoles(models.IntegerChoices):
        CommunityManager = 1
        Admin = 2
        Moderator = 3
        ProductExpert = 4
        Trainer = 5
        Editor = 6
        BlogContentExpert = 7
        Other = 10

    fullName = models.CharField(
        verbose_name=_("full name"),
        max_length=60,
        validators=[MinLengthValidator(4)],
        unique=True,
    )
    emailAddress = models.EmailField(verbose_name=_("email address"), unique=True)
    profileImageURL = models.URLField(
        verbose_name=_("profile image url"),
        max_length=200,
        blank=True,
        default="",
        help_text=_("profile image of the member."),
    )
    joinDate = models.DateTimeField(verbose_name=_("join date"), auto_now_add=True)
    bigCommandId = models.UUIDField(
        verbose_name=_("BigCommand ID"),
        help_text=_("the  bigcommand userId of this member"),
    )
    publicName = models.CharField(
        verbose_name=_("public name"),
        max_length=50,
        help_text=_("the member's public name used instead of their full names."),
        unique=True,
    )
    roles = ArrayField(
        verbose_name=_("roles"),
        base_field=models.PositiveSmallIntegerField(choices=MemberRoles.choices),
        blank=True,
        default=list,
        help_text=_("members roles"),
    )
    followers = models.ManyToManyField(
        verbose_name=_("followers"),
        to="self",
        symmetrical=False,
        blank=True,
        help_text=_("other members following this member."),
        related_name="memberFollowings",
        related_query_name="memberFollowing",
    )
    following = models.ManyToManyField(
        verbose_name=_("following"),
        to="self",
        symmetrical=False,
        blank=True,
        help_text=_("other members this member is following."),
        related_name="memberFollowers",
        related_query_name="memberFollower",
    )

    class Meta:
        verbose_name = _("member")
        verbose_name_plural = _("members")
        indexes = [
            models.Index(fields=["fullName"]),
            models.Index(fields=["emailAddress"]),
        ]
        unique_together = ["fullName", "emailAddress"]
        default_permissions = []

    def __str__(self):
        return self.fullName

    def get_absolute_url(self):
        return reverse("member-detail", args=[str(self.pk)])


class Comment(models.Model):
    creationDate = models.DateTimeField(
        verbose_name=_("creation date"),
        auto_now_add=True,
    )
    lastModifiedDate = models.DateTimeField(
        verbose_name=_("last modified date"), auto_now=True
    )
    author = models.ForeignKey(
        verbose_name=_("author"),
        to=Member,
        on_delete=models.SET_NULL,
        null=True,
        help_text=_("comment author. Should be a Member model."),
        related_name="comments",
        related_query_name="comment",
    )
    content = models.TextField(verbose_name=_("content"))
    parent = models.ForeignKey(
        verbose_name=_("replies"),
        to="self",
        on_delete=models.CASCADE,
        null=True,
        related_name="replies",
        related_query_name="reply",
        help_text=_(
            "null indicates this is a root comment, else, the field should point to the comment being replied to."
        ),
    )
    likes = models.PositiveIntegerField(
        verbose_name=_("likes"),
        default=0,
        editable=False,
        help_text=_("comment likes."),
    )

    class Meta:
        verbose_name = _("comment")
        verbose_name_plural = _("comments")
        ordering = ["-creationDate"]
        indexes = [
            models.Index(fields=["-creationDate"]),
        ]
        default_permissions = []

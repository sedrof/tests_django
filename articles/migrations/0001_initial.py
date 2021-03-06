# Generated by Django 3.2.2 on 2021-05-09 22:33

import django.contrib.postgres.fields
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("en", "En"),
                            ("es", "Es"),
                            ("fr", "Fr"),
                            ("pt", "Pt"),
                            ("zh-Hans", "Zhhans"),
                            ("zh-Hant", "Zhhant"),
                        ],
                        default="en",
                        help_text="the language this content is in.",
                        max_length=10,
                        verbose_name="language",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=150,
                        validators=[django.core.validators.MinLengthValidator(2)],
                        verbose_name="title",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        allow_unicode=True,
                        help_text="the content slug. Accepts unicode characters.",
                        max_length=150,
                        unique=True,
                        verbose_name="slug",
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        help_text="the html body content of the article.",
                        verbose_name="content",
                    ),
                ),
                (
                    "publishDate",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="publish date"
                    ),
                ),
                (
                    "lastModifiedDate",
                    models.DateTimeField(
                        auto_now=True, verbose_name="last modified date"
                    ),
                ),
                (
                    "isHelpFulCount",
                    models.IntegerField(
                        default=0,
                        editable=False,
                        help_text="how many viewers found this article helpful.",
                        verbose_name="is helpful count",
                    ),
                ),
                (
                    "isNotHelpFulCount",
                    models.IntegerField(
                        default=0,
                        editable=False,
                        help_text="how many viewers did not find this article helpful.",
                        verbose_name="is not helpful count",
                    ),
                ),
            ],
            options={
                "verbose_name": "article",
                "verbose_name_plural": "articles",
                "abstract": False,
                "default_permissions": [],
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("en", "En"),
                            ("es", "Es"),
                            ("fr", "Fr"),
                            ("pt", "Pt"),
                            ("zh-Hans", "Zhhans"),
                            ("zh-Hant", "Zhhant"),
                        ],
                        default="en",
                        help_text="the language this content is in.",
                        max_length=10,
                        verbose_name="language",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=150,
                        validators=[django.core.validators.MinLengthValidator(2)],
                        verbose_name="title",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="optional description for this category.",
                        max_length=200,
                        verbose_name="description",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        allow_unicode=True,
                        help_text="the topic category slug. Accepts unicode characters.",
                        max_length=150,
                        unique=True,
                        verbose_name="slug",
                    ),
                ),
                (
                    "app",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "Home"),
                            (2, "Account"),
                            (3, "Boomfront"),
                            (4, "Boomaffiliate"),
                            (5, "Inboxbird"),
                            (6, "Adilo"),
                            (7, "Huula"),
                            (8, "Bigdrive"),
                            (9, "Contacts"),
                            (10, "Uvendi"),
                            (11, "Portal"),
                            (12, "Helpcenter"),
                            (13, "Bigpartner"),
                            (14, "Corina"),
                            (100, "Platform"),
                        ],
                        help_text="the BigCommand app ID this category apply to. Required for relevance filtering.",
                        null=True,
                        verbose_name="app",
                    ),
                ),
                (
                    "englishVersion",
                    models.ForeignKey(
                        help_text="\n            references the english version of the content. This enables to \n            find the content translation in a different language.\n            ",
                        limit_choices_to={"language": "en"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="translations",
                        related_query_name="translation",
                        to="articles.category",
                        verbose_name="english version",
                    ),
                ),
            ],
            options={
                "verbose_name": "categories",
                "verbose_name_plural": "category",
                "default_permissions": [],
            },
        ),
        migrations.CreateModel(
            name="Topic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("en", "En"),
                            ("es", "Es"),
                            ("fr", "Fr"),
                            ("pt", "Pt"),
                            ("zh-Hans", "Zhhans"),
                            ("zh-Hant", "Zhhant"),
                        ],
                        default="en",
                        help_text="the language this content is in.",
                        max_length=10,
                        verbose_name="language",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=150,
                        validators=[django.core.validators.MinLengthValidator(2)],
                        verbose_name="title",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="optional description for this topic.",
                        max_length=200,
                        verbose_name="description",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        allow_unicode=True,
                        help_text="the topic slug. Accepts unicode characters.",
                        max_length=150,
                        unique=True,
                        verbose_name="slug",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        help_text="the category this topic belongs to.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="topics",
                        related_query_name="topic",
                        to="articles.category",
                        verbose_name="category",
                    ),
                ),
                (
                    "englishVersion",
                    models.ForeignKey(
                        help_text="\n            references the english version of the content. This enables to \n            find the content translation in a different language.\n            ",
                        limit_choices_to={"language": "en"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="translations",
                        related_query_name="translation",
                        to="articles.topic",
                        verbose_name="english version",
                    ),
                ),
            ],
            options={
                "verbose_name": "topic",
                "verbose_name_plural": "topics",
                "abstract": False,
                "default_permissions": [],
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("en", "En"),
                            ("es", "Es"),
                            ("fr", "Fr"),
                            ("pt", "Pt"),
                            ("zh-Hans", "Zhhans"),
                            ("zh-Hant", "Zhhant"),
                        ],
                        default="en",
                        help_text="the language this content is in.",
                        max_length=10,
                        verbose_name="language",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=50, unique=True, verbose_name="name"),
                ),
                (
                    "englishVersion",
                    models.ForeignKey(
                        help_text="\n            references the english version of the content. This enables to \n            find the content translation in a different language.\n            ",
                        limit_choices_to={"language": "en"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="translations",
                        related_query_name="translation",
                        to="articles.tag",
                        verbose_name="english version",
                    ),
                ),
            ],
            options={
                "verbose_name": "tag",
                "verbose_name_plural": "tags",
                "abstract": False,
                "default_permissions": [],
            },
        ),
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fullName",
                    models.CharField(
                        max_length=60,
                        unique=True,
                        validators=[django.core.validators.MinLengthValidator(4)],
                        verbose_name="full name",
                    ),
                ),
                (
                    "emailAddress",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email address"
                    ),
                ),
                (
                    "profileImageURL",
                    models.URLField(
                        blank=True,
                        default="",
                        help_text="profile image of the member.",
                        verbose_name="profile image url",
                    ),
                ),
                (
                    "joinDate",
                    models.DateTimeField(auto_now_add=True, verbose_name="join date"),
                ),
                (
                    "bigCommandId",
                    models.UUIDField(
                        help_text="the  bigcommand userId of this member",
                        verbose_name="BigCommand ID",
                    ),
                ),
                (
                    "publicName",
                    models.CharField(
                        help_text="the member's public name used instead of their full names.",
                        max_length=50,
                        unique=True,
                        verbose_name="public name",
                    ),
                ),
                (
                    "roles",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.PositiveSmallIntegerField(
                            choices=[
                                (1, "Communitymanager"),
                                (2, "Admin"),
                                (3, "Moderator"),
                                (4, "Productexpert"),
                                (5, "Trainer"),
                                (6, "Editor"),
                                (10, "Other"),
                            ]
                        ),
                        blank=True,
                        default=list,
                        help_text="members roles",
                        size=None,
                        verbose_name="roles",
                    ),
                ),
                (
                    "followers",
                    models.ManyToManyField(
                        blank=True,
                        help_text="other members following this member.",
                        related_name="memberFollowings",
                        related_query_name="memberFollowing",
                        to="articles.Member",
                        verbose_name="followers",
                    ),
                ),
                (
                    "following",
                    models.ManyToManyField(
                        blank=True,
                        help_text="other members this member is following.",
                        related_name="memberFollowers",
                        related_query_name="memberFollower",
                        to="articles.Member",
                        verbose_name="following",
                    ),
                ),
            ],
            options={
                "verbose_name": "member",
                "verbose_name_plural": "members",
                "default_permissions": [],
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "creationDate",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="creation date"
                    ),
                ),
                (
                    "lastModifiedDate",
                    models.DateTimeField(
                        auto_now=True, verbose_name="last modified date"
                    ),
                ),
                ("content", models.TextField(verbose_name="content")),
                (
                    "likes",
                    models.IntegerField(
                        default=0,
                        editable=False,
                        help_text="comment likes.",
                        verbose_name="likes",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        help_text="comment author. Should be a Member model.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="articles.member",
                        verbose_name="author",
                    ),
                ),
                (
                    "replies",
                    models.ManyToManyField(
                        blank=True,
                        help_text="comment replies.",
                        to="articles.Comment",
                        verbose_name="replies",
                    ),
                ),
            ],
            options={
                "verbose_name": "comment",
                "verbose_name_plural": "comments",
                "ordering": ["-creationDate"],
                "default_permissions": [],
            },
        ),
        migrations.CreateModel(
            name="ArticleView",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True, verbose_name="date")),
                (
                    "userId",
                    models.UUIDField(
                        editable=False,
                        help_text="id of the BigCommand user if authenticated.",
                        null=True,
                        verbose_name="created by",
                    ),
                ),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="views",
                        related_query_name="view",
                        to="articles.article",
                        verbose_name="article",
                    ),
                ),
            ],
            options={
                "verbose_name": "article view",
                "verbose_name_plural": "article views",
                "default_permissions": [],
            },
        ),
        migrations.AddField(
            model_name="article",
            name="authors",
            field=models.ManyToManyField(
                help_text="all authors who contributed to this article.",
                related_name="articles",
                related_query_name="article",
                to="articles.Member",
                verbose_name="author",
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="englishVersion",
            field=models.ForeignKey(
                help_text="\n            references the english version of the content. This enables to \n            find the content translation in a different language.\n            ",
                limit_choices_to={"language": "en"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="translations",
                related_query_name="translation",
                to="articles.article",
                verbose_name="english version",
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="tags",
            field=models.ManyToManyField(
                blank=True,
                related_name="articles",
                related_query_name="article",
                to="articles.Tag",
                verbose_name="tags",
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="topic",
            field=models.ForeignKey(
                help_text="the topic this article belongs to.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="articles",
                related_query_name="article",
                to="articles.topic",
                verbose_name="topic",
            ),
        ),
        migrations.AddIndex(
            model_name="topic",
            index=models.Index(
                fields=["language"], name="articles_to_languag_4cf090_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="tag",
            index=models.Index(fields=["name"], name="articles_ta_name_917d3f_idx"),
        ),
        migrations.AddIndex(
            model_name="member",
            index=models.Index(
                fields=["fullName"], name="articles_me_fullNam_7850b2_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="member",
            index=models.Index(
                fields=["emailAddress"], name="articles_me_emailAd_34ada7_idx"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="member",
            unique_together={("fullName", "emailAddress")},
        ),
        migrations.AddIndex(
            model_name="comment",
            index=models.Index(
                fields=["-creationDate"], name="articles_co_creatio_ea3599_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="category",
            index=models.Index(fields=["slug"], name="articles_ca_slug_984c4d_idx"),
        ),
        migrations.AddIndex(
            model_name="category",
            index=models.Index(
                fields=["language"], name="articles_ca_languag_0b8262_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="category",
            index=models.Index(fields=["app"], name="articles_ca_app_3b4fd1_idx"),
        ),
        migrations.AddIndex(
            model_name="articleview",
            index=models.Index(fields=["date"], name="articles_ar_date_8fa2fb_idx"),
        ),
        migrations.AddIndex(
            model_name="article",
            index=models.Index(
                fields=["language"], name="articles_ar_languag_22b89d_idx"
            ),
        ),
    ]

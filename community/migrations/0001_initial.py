# Generated by Django 3.2.2 on 2021-05-09 22:33

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
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
                    "description",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="optional description for this content.",
                        max_length=200,
                        verbose_name="description",
                    ),
                ),
                (
                    "thumbnailURL",
                    models.URLField(
                        blank=True,
                        default="",
                        help_text="optional category thumbnail.",
                        verbose_name="thumbnail url",
                    ),
                ),
            ],
            options={
                "verbose_name": "category",
                "verbose_name_plural": "categories",
                "default_permissions": [],
            },
        ),
        migrations.CreateModel(
            name="Post",
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
                        help_text="the html body content of the post.",
                        verbose_name="content",
                    ),
                ),
                (
                    "thumbnailURL",
                    models.URLField(
                        blank=True,
                        default="",
                        help_text="optional post thumbnail url.",
                        verbose_name="thumbnail url",
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
                    "allowComments",
                    models.BooleanField(default=False, verbose_name="allow comments"),
                ),
                (
                    "isPinned",
                    models.BooleanField(
                        default=False,
                        help_text="pinned posts stick to the top.",
                        verbose_name="is pinned",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="articles.member",
                        verbose_name="author",
                    ),
                ),
                (
                    "category",
                    models.ManyToManyField(
                        help_text="the category this post belongs to.",
                        to="community.Category",
                        verbose_name="category",
                    ),
                ),
                (
                    "comments",
                    models.ManyToManyField(
                        blank=True, to="articles.Comment", verbose_name="comments"
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True,
                        related_name="communityPosts",
                        related_query_name="communityPost",
                        to="articles.Tag",
                        verbose_name="tags",
                    ),
                ),
            ],
            options={
                "verbose_name": "post",
                "verbose_name_plural": "posts",
                "ordering": ["-publishDate"],
                "default_permissions": [],
            },
        ),
        migrations.CreateModel(
            name="PostView",
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
                    "durationOnPage",
                    models.DurationField(null=True, verbose_name="duration on page"),
                ),
                (
                    "percentageRead",
                    models.DecimalField(
                        decimal_places=1,
                        max_digits=4,
                        null=True,
                        verbose_name="percentage read",
                    ),
                ),
                (
                    "isUnique",
                    models.BooleanField(default=True, verbose_name="is unique"),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="posts",
                        related_query_name="post",
                        to="community.post",
                        verbose_name="post",
                    ),
                ),
            ],
            options={
                "verbose_name": "post view",
                "verbose_name_plural": "post views",
                "default_permissions": [],
            },
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(
                fields=["-publishDate"], name="community_p_publish_469a22_idx"
            ),
        ),
    ]

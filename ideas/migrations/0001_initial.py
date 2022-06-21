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
            name="FeatureRequest",
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
                        help_text="the body content of the post.",
                        verbose_name="content",
                    ),
                ),
                (
                    "featuredImageURL",
                    models.URLField(
                        blank=True,
                        default="",
                        help_text="optional featured image url.",
                        verbose_name="featured image url",
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
                    "level",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "Nicetohave"), (2, "Important"), (3, "Critical")],
                        default=2,
                        help_text="how critical is this feature.",
                        verbose_name="criticality level",
                    ),
                ),
                (
                    "phase",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "Underreview"),
                            (2, "Inroadmap"),
                            (3, "Betarelease"),
                            (4, "Launched"),
                            (5, "Cancelled"),
                        ],
                        default=1,
                        help_text="current phase pf this feature request.",
                        verbose_name="phase",
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
                        help_text="the bigcommand app ID this feature request applies to.",
                        verbose_name="app",
                    ),
                ),
                (
                    "isPinned",
                    models.BooleanField(
                        default=False,
                        help_text="pinned feature requests stick to the top.",
                        verbose_name="is pinned",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="featureRequests",
                        related_query_name="featureRequest",
                        to="articles.member",
                        verbose_name="author",
                    ),
                ),
                (
                    "comments",
                    models.ManyToManyField(
                        blank=True,
                        related_name="featureRequests",
                        related_query_name="featureRequest",
                        to="articles.Comment",
                        verbose_name="comments",
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True,
                        related_name="featureRequests",
                        related_query_name="featureRequest",
                        to="articles.Tag",
                        verbose_name="tags",
                    ),
                ),
            ],
            options={
                "verbose_name": "feature requests",
                "verbose_name_plural": "feature request",
                "ordering": ["-publishDate"],
                "default_permissions": [],
            },
        ),
        migrations.CreateModel(
            name="Vote",
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
                    "date",
                    models.DateTimeField(auto_now_add=True, verbose_name="vote date"),
                ),
                (
                    "featureRequest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="votes",
                        related_query_name="vote",
                        to="ideas.featurerequest",
                        verbose_name="feature request",
                    ),
                ),
                (
                    "voter",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="featureVotes",
                        related_query_name="featureVote",
                        to="articles.member",
                        verbose_name="voter",
                    ),
                ),
            ],
            options={
                "verbose_name": "vote",
                "verbose_name_plural": "votes",
                "ordering": ["-date"],
                "default_permissions": [],
            },
        ),
        migrations.CreateModel(
            name="RoadMap",
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
                    "devStartDate",
                    models.DateField(null=True, verbose_name="development start date"),
                ),
                (
                    "expectedReleaseDate",
                    models.DateField(null=True, verbose_name="expected release date"),
                ),
                (
                    "feature",
                    models.OneToOneField(
                        limit_choices_to={"phase": 2},
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ideas.featurerequest",
                        verbose_name="feature",
                    ),
                ),
            ],
            options={
                "verbose_name": "roadmap",
                "verbose_name_plural": "roadmaps",
                "ordering": ["-devStartDate"],
                "default_permissions": [],
            },
        ),
        migrations.AddIndex(
            model_name="vote",
            index=models.Index(fields=["-date"], name="ideas_vote_date_419514_idx"),
        ),
        migrations.AddIndex(
            model_name="roadmap",
            index=models.Index(
                fields=["-devStartDate"], name="ideas_roadm_devStar_13b3e7_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="roadmap",
            index=models.Index(
                fields=["-expectedReleaseDate"], name="ideas_roadm_expecte_cdee72_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="featurerequest",
            index=models.Index(fields=["level"], name="ideas_featu_level_c9db91_idx"),
        ),
        migrations.AddIndex(
            model_name="featurerequest",
            index=models.Index(fields=["phase"], name="ideas_featu_phase_e5fcb5_idx"),
        ),
        migrations.AddIndex(
            model_name="featurerequest",
            index=models.Index(fields=["app"], name="ideas_featu_app_7469f2_idx"),
        ),
        migrations.AddIndex(
            model_name="featurerequest",
            index=models.Index(
                fields=["-publishDate"], name="ideas_featu_publish_bf68e8_idx"
            ),
        ),
    ]
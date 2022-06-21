# Generated by Django 3.2.2 on 2021-05-11 03:34

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0002_auto_20210510_0012"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="roles",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.PositiveSmallIntegerField(
                    choices=[
                        (1, "Communitymanager"),
                        (2, "Admin"),
                        (3, "Moderator"),
                        (4, "Productexpert"),
                        (5, "Trainer"),
                        (6, "Editor"),
                        (7, "Blogcontentexpert"),
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
    ]
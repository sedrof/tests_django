# Generated by Django 3.2.2 on 2021-05-11 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ideas", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="featurerequest",
            name="isPublic",
            field=models.BooleanField(
                default=False,
                help_text="public feature request will show up in public portal.",
                verbose_name="is public",
            ),
        ),
        migrations.AddField(
            model_name="roadmap",
            name="isPublic",
            field=models.BooleanField(
                default=False,
                help_text="is this roadmap public.",
                verbose_name="is public",
            ),
        ),
    ]
from datetime import datetime

from django.test import TestCase

from django.utils import timezone

from guides.models import Topic, Category, Lesson
from includes.common.bigcommand_apps import BigCommandApps


class LearningProgressTestCase(TestCase):
    @classmethod
    def setUp(cls):

        cls.test_category = Category.objects.create(
            title="test_category_title",
            slug="test_category_slug",
            app=BigCommandApps.Adilo,
            description="test_category_describtion",
            thumbnailURL="https://link.com/",
        )

        cls.test_topic = Topic.objects.create(
            title="test_topic_title_for_guide",
            description="test_topic_describtion",
            category=cls.test_category
        )

    def test_model_fields(self):
        self.assertEqual(self.test_topic.title, 'test_topic_title_for_guide')
        self.assertEqual(self.test_topic.description, 'test_topic_describtion')

    def test_string_representation(self):
        self.assertEqual(str(self.test_topic), 'test_topic_title_for_guide')

    def save_slug_on_creation(self):
        self.assertEqual(self.test_topic.slug, "test_topic_title_for_guide")

    def test_model_absolute_url(self):
        self.assertEqual(
            self.test_topic.get_absolute_url(),
            f"/api/v1/guides/topics/{self.test_topic.slug}/",
        )

    def test_verbose_names(self):
        self.assertEqual(self.test_topic._meta.verbose_name, "topic")
        self.assertEqual(self.test_topic._meta.verbose_name_plural, "topics")
from django.test import TestCase

from articles.models import Topic
from articles.tests.test_member import initialize_category
from includes.common.supported_languages import SupportedLanguages


class TagsTestCase(TestCase):
    @classmethod
    def setUp(cls):

        cls.test_category = initialize_category()
        cls.test_topic = Topic.objects.create(
            description='test_topic', category=cls.test_category,
            title='test_topic_title', language=SupportedLanguages.EN)
    def test_model_fields(self):
        self.assertEqual(self.test_topic.description, "test_topic")
        self.assertEqual(self.test_topic.title, "test_topic_title")
        self.assertEqual(self.test_topic.language, SupportedLanguages.EN)


    def test_string_representation(self):
        self.assertEqual(str(self.test_topic), "test_topic_title")

    def test_model_is_assigned_slug_on_creation(self):
        self.assertEqual(self.test_topic.slug, "test_topic_title")

    def test_model_absolute_url(self):
        self.assertEqual(
            self.test_topic.get_absolute_url(),
            f"/api/v1/topics/{self.test_topic.slug}/",
        )

    def test_verbose_names(self):
        verbose_name = self.test_topic._meta.verbose_name
        verbose_name_plural = self.test_topic._meta.verbose_name_plural
        self.assertEqual(verbose_name, "topic")
        self.assertEqual(verbose_name_plural, "topics")

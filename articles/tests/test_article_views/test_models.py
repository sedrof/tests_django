import uuid

from datetime import datetime

from django.test import TestCase

from articles.models.articles import Article
from articles.tests.test_member import (
    initialize_member,
    initialize_topic,
    initialize_tag,
)

from articles.models.articles import ArticleView


class ArticleViewTestCase(TestCase):
    @classmethod
    def setUp(cls):
        cls.test_member_model = initialize_member()
        cls.test_tag_model = initialize_tag()
        cls.test_topic_model = initialize_topic()

        cls.test_artice_model = Article.objects.create(
            content="test_content_1",
            isHelpFulCount="22",
            isNotHelpFulCount="44",
            topic=cls.test_topic_model,
            title="test_article_title",
        )
        cls.test_artice_model.authors.set([cls.test_member_model])
        cls.test_artice_model.tags.set([cls.test_tag_model])

        cls.test_article = ArticleView.objects.create(
            ipAddress="192.168.0.1",
            userId=str(uuid.uuid4()),
            article=cls.test_artice_model,
        )

    def test_model_fields(self):
        self.assertEqual(self.test_article.ipAddress, "192.168.0.1")
        self.assertIsInstance(self.test_article.date, datetime)
        self.assertEqual(self.test_article.userId, "12345678123456781234567812345678")

    def test_string_representation(self):
        self.assertEqual(
            str(self.test_article),
            "View for" + " " + f"'{self.test_artice_model.title}'",
        )

    def test_article_verbose_names(self):
        self.assertEqual(self.test_article._meta.verbose_name, "article view")
        self.assertEqual(self.test_article._meta.verbose_name_plural, "article views")

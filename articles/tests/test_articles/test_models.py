from datetime import datetime
import uuid
from django.test import TestCase

from django.utils import timezone
from articles.tests.test_member import (
    initialize_member,
    initialize_topic,
    initialize_tag,
)
from articles.models.articles import Article


class ArticleTestCase(TestCase):
    @classmethod
    def setUp(cls):

        cls.test_member_model = initialize_member()

        cls.test_tag_model = initialize_tag('tag1')

        cls.test_topic_model = initialize_topic()
        cls.now = timezone.now()

        cls.test_article = Article.objects.create(
            # authors=cls.bigCommandId,
            content="test_content_1",
            isHelpFulCount="22",
            isNotHelpFulCount="44",
            topic=cls.test_topic_model,
            title="test_article_title",
            lastModifiedDate=cls.now
        )

        cls.test_article.authors.set([cls.test_member_model])
        cls.test_article.tags.set([cls.test_tag_model])

    def test_model_fields(self):
        self.assertEqual(self.test_article.title, "test_article_title")
        self.assertIsInstance(self.test_article.lastModifiedDate, datetime)
        self.assertEqual(self.test_article.content, "test_content_1")
        self.assertEqual(self.test_article.isHelpFulCount, "22")
        self.assertEqual(self.test_article.isNotHelpFulCount, "44")

    def test_string_representation(self):
        self.assertEqual(str(self.test_article), "test_article_title")

    def test_model_is_assigned_slug_on_creation(self):
        self.assertEqual(self.test_article.slug, "test_article_title")

    def test_model_absolute_url(self):
        self.assertEqual(
            self.test_article.get_absolute_url(),
            f"/api/v1/articles/{self.test_article.slug}/",
        )

    def test_article_verbose_names(self):
        self.assertEqual(self.test_article._meta.verbose_name, "article")
        self.assertEqual(self.test_article._meta.verbose_name_plural, "articles")

    def test_many_to_many_field_with_authors(self):
        self.assertEqual(self.test_article.authors.count(), 1)

    def test_many_to_many_field_with_tags(self):
        self.assertEqual(self.test_article.tags.count(), 1)

    def test_related_articles(self):
        test_tag_model_2 = initialize_tag('tag2')
        # self.assertEqual(self.test_article.tags, self.test_article.all())
        self.assertIn(self.test_tag_model, self.test_article.tags.all())
from datetime import datetime
from django.test import TestCase

from django.utils import timezone

from articles.models.common import Comment
from articles.tests.test_member import (
    initialize_member,
    initialize_tag,
)
from community.models import Post, Category


class ArticleTestCase(TestCase):
    @classmethod
    def setUp(cls):
        cls.now = timezone.now()

        cls.test_member_model = initialize_member()

        cls.test_tag_model = initialize_tag("post_tag")


        cls.test_comment = Comment.objects.create(
            content="test_content_field",
        )

        cls.test_category = Category.objects.create(
            title="test_post_category_title",
        )

        cls.test_post = Post.objects.create(
            title="test_post_title",
            content="test_post",
            thumbnailURL="https://link.com/",
            publishDate=cls.now,
            lastModifiedDate=cls.now,
            allowComments=False,
            isPinned=False,
            author=cls.test_member_model
        )

        cls.test_post.tags.set([cls.test_tag_model])
        cls.test_post.comments.set([cls.test_comment])

    def test_model_fields(self):
        self.assertEqual(self.test_post.title, "test_post_title")
        self.assertEqual(self.test_post.content, "test_post")
        self.assertEqual(self.test_post.thumbnailURL, "https://link.com/")
        self.assertIsInstance(self.test_post.publishDate, datetime)
        self.assertIsInstance(self.test_post.lastModifiedDate, datetime)
        self.assertEqual(self.test_post.allowComments, False)
        self.assertEqual(self.test_post.isPinned, False)

    def test_string_representation(self):
        self.assertEqual(str(self.test_post), "test_post_title")
    #
    def test_model_is_assigned_slug_on_creation(self):
        self.assertEqual(self.test_post.slug, "test_post_title")
    #
    def test_model_absolute_url(self):
        self.assertEqual(
            self.test_post.get_absolute_url(),
            f"/api/v1/community/{self.test_post.slug}/",
        )
    #
    def test_verbose_names(self):
        self.assertEqual(self.test_post._meta.verbose_name, "post")
        self.assertEqual(self.test_post._meta.verbose_name_plural, "posts")
    #
    def test_many_to_many_field_with_comments(self):
        self.assertEqual(self.test_post.comments.count(), 1)

    def test_many_to_many_field_with_tags(self):
        self.assertEqual(self.test_post.tags.count(), 1)

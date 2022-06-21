from django.test import TestCase
from django.utils import timezone

from datetime import datetime
from articles.models.common import Comment
from articles.tests.test_member import initialize_member


class CommentTestCase(TestCase):
    @classmethod
    def setUp(cls):

        cls.test_member = initialize_member()
        cls.now = timezone.now()
        cls.test_comment_parent = Comment.objects.create(
            creationDate=datetime,
            lastModifiedDate=datetime,
            author=cls.test_member,
            content="test_content_field",

        )

        cls.test_comment_reply = Comment.objects.create(
            creationDate=cls.now,
            lastModifiedDate=cls.now,
            author=cls.test_member,
            content="test_content_field",
            likes="15",
            parent=cls.test_comment_parent,
        )

    def test_model_fields(self):
        self.assertIsInstance(self.test_comment_reply.creationDate, datetime)
        self.assertIsInstance(self.test_comment_reply.lastModifiedDate, datetime)
        self.assertEqual(self.test_comment_reply.author, self.test_member)
        self.assertEqual(self.test_comment_reply.content, "test_content_field")
        self.assertEqual(self.test_comment_reply.likes, "15")
        self.assertEqual(self.test_comment_reply.parent, self.test_comment_parent)

    def test_category_verbose_names(self):
        self.assertEqual(self.test_comment_reply._meta.verbose_name, "comment")
        self.assertEqual(self.test_comment_reply._meta.verbose_name_plural, "comments")

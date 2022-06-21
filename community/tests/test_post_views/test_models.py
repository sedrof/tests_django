from datetime import datetime
from django.test import TestCase

from django.utils import timezone

from community.models import Post, PostView


class PostViewTestCase(TestCase):
    @classmethod
    def setUp(cls):
        cls.now = timezone.now()

        cls.test_post = Post.objects.create(
            title="test_post_title",
        )

        cls.test_post_view = PostView.objects.create(
            post=cls.test_post,
            date=cls.now,
            durationOnPage='41:15:20',
            percentageRead='80',
            isUnique=False,
            ipAddress='192.168.0.1'
        )

    def test_model_fields(self):
        self.assertIsInstance(self.test_post_view.date, datetime)
        self.assertEqual(self.test_post_view.durationOnPage, '41:15:20')
        self.assertEqual(self.test_post_view.percentageRead, '80')
        self.assertEqual(self.test_post_view.isUnique, False)
        self.assertEqual(self.test_post_view.ipAddress, '192.168.0.1')

    def test_string_representation(self):
        self.assertEqual(str(self.test_post_view), "View for" + " " + f"'{self.test_post_view.post.title}'")



    def test_model_absolute_url(self):
        self.assertEqual(
            self.test_post_view.get_absolute_url(),
            f"/api/v1/community/views/{self.test_post_view.pk}/",
        )

    def test_verbose_names(self):
        self.assertEqual(self.test_post_view._meta.verbose_name, "post view")
        self.assertEqual(self.test_post_view._meta.verbose_name_plural, "post views")


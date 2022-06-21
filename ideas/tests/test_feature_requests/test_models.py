from datetime import datetime

from django.test import TestCase

from articles.models import Comment
from articles.tests.test_member import (
    initialize_member,
    initialize_tag,
)
from ideas.models import FeatureRequest
from includes.common.bigcommand_apps import BigCommandApps


class GuideTestCase(TestCase):
    @classmethod
    def setUp(cls):

        cls.test_author = initialize_member()
        cls.test_comment_parent = Comment.objects.create(
            lastModifiedDate=datetime,
            author=cls.test_author,
            content="test_content_field",

        )

        cls.test_comment_reply = Comment.objects.create(
            author=cls.test_author,
            content="test_content_field",
            likes="15",
            parent=cls.test_comment_parent,
        )

        cls.test_tags = initialize_tag('tag_guide_test')

        cls.test_feauture_request = FeatureRequest.objects.create(
            title="test_test_feauture_request",
            content="test_est_feauture_request_content",
            featuredImageURL=False,
            app=BigCommandApps.Home,
            author=cls.test_author
        )

        cls.test_feauture_request.comments.set([cls.test_comment_reply])
        cls.test_feauture_request.tags.set([cls.test_tags])


    def test_model_fields(self):
        self.assertEqual(self.test_feauture_request.title, "test_test_feauture_request")
    #     self.assertEqual(self.test_guide.description, "test_guide_description")
    #     self.assertEqual(self.test_guide.isPinned, False)
    #
    #
    # def test_string_representation(self):
    #     self.assertEqual(str(self.test_guide), "test_guide_title")
    #
    #
    #
    # # def test_model_absolute_url(self):
    # #     self.assertEqual(
    # #         self.test_guide.get_absolute_url(),
    # #         f"/api/v1/guides/{self.test_guide.pk}/",
    # #     )
    #
    # def test_article_verbose_names(self):
    #     self.assertEqual(self.test_guide._meta.verbose_name, "guide")
    #     self.assertEqual(self.test_guide._meta.verbose_name_plural, "guides")
    #
    # def test_many_to_many_field_with_creators(self):
    #     self.assertEqual(self.test_guide.creators.count(), 1)
    #
    # def test_many_to_many_field_with_tags(self):
    #     self.assertEqual(self.test_guide.tags.count(), 1)
    #
    # def test_many_to_many_field_with_lessons(self):
    #     self.assertEqual(self.test_guide.lessons.count(), 1)



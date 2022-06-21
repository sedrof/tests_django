from datetime import datetime

from django.test import TestCase

from django.utils import timezone
from articles.tests.test_member import (
    initialize_member,
    initialize_tag,
)

from guides.models import Guide, Lesson, Topic


class GuideTestCase(TestCase):
    @classmethod
    def setUp(cls):

        cls.test_creators = initialize_member()

        cls.test_tags = initialize_tag('tag_guide_test')

        cls.test_topic = Topic.objects.create(
            title="test_topic_title_for_guide"
        )

        cls.now = timezone.now()

        cls.test_lessons = Lesson.objects.create(
            content="test_lesson_content",
            stepNumber=1
        )

        cls.test_guide = Guide.objects.create(
            title="test_guide_title",
            description="test_guide_description",
            isPinned=False,
            topic=cls.test_topic
        )

        cls.test_guide.creators.set([cls.test_creators])
        cls.test_guide.tags.set([cls.test_tags])
        cls.test_guide.lessons.set([cls.test_lessons])

    def test_model_fields(self):
        self.assertEqual(self.test_guide.title, "test_guide_title")
        self.assertEqual(self.test_guide.description, "test_guide_description")
        self.assertEqual(self.test_guide.isPinned, False)


    def test_string_representation(self):
        self.assertEqual(str(self.test_guide), "test_guide_title")



    # def test_model_absolute_url(self):
    #     self.assertEqual(
    #         self.test_guide.get_absolute_url(),
    #         f"/api/v1/guides/{self.test_guide.pk}/",
    #     )

    def test_article_verbose_names(self):
        self.assertEqual(self.test_guide._meta.verbose_name, "guide")
        self.assertEqual(self.test_guide._meta.verbose_name_plural, "guides")

    def test_many_to_many_field_with_creators(self):
        self.assertEqual(self.test_guide.creators.count(), 1)

    def test_many_to_many_field_with_tags(self):
        self.assertEqual(self.test_guide.tags.count(), 1)

    def test_many_to_many_field_with_lessons(self):
        self.assertEqual(self.test_guide.lessons.count(), 1)



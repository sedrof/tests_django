import uuid

from datetime import datetime

from django.test import TestCase

from django.utils import timezone

from guides.models import Guide, Student, Topic, Category, Lesson
from includes.common.bigcommand_apps import BigCommandApps


class LearningProgressTestCase(TestCase):
    @classmethod
    def setUp(cls):

        cls.test_lessons_viewed_guide = Lesson.objects.create(
            content="test_lesson_content",
            stepNumber=1
        )
        cls.test_category = Category.objects.create(
            title="test_category_title",
            slug="test_category_slug",
            app=BigCommandApps.Adilo,
            description="test_category_describtion",
            thumbnailURL="https://link.com/",
        )

        cls.test_topic = Topic.objects.create(
            title="test_topic_title_for_guide",
            category=cls.test_category
        )

        cls.test_viewed_guide = Guide.objects.create(
            title="test_guide_title",
            description="test_guide_description",
            isPinned=False,
            topic=cls.test_topic
        )

        cls.test_viewed_guide.lessons.set([cls.test_lessons_viewed_guide])

        cls.test_saved_guide = Guide.objects.create(
            title="test_guide_title",
            description="test_guide_description",
            isPinned=False,
            topic=cls.test_topic
        )

        cls.now = timezone.now()

        cls.test_student = Student.objects.create(
            fullName="test_full_name",
            publicName="test_public_name",
            bigCommandId=str(uuid.uuid4())
        )

        cls.test_student.viewedGuides.set([cls.test_viewed_guide])
        cls.test_student.savedGuides.set([cls.test_saved_guide])


    def test_model_fields(self):
        self.assertEqual(self.test_student.fullName, "test_full_name")
    #     self.assertEqual(self.test_student.lessonsCompleted, 1)
    #     self.assertIsInstance(self.test_student.completionDate, datetime)
    #
    #
    #
    # def test_string_representation(self):
    #     self.assertEqual(str(self.test_student), "test_full_name's learning progress")
    #
    #
    #
    # def test_model_absolute_url(self):
    #     self.assertEqual(
    #         self.test_student.get_absolute_url(),
    #         f"/api/v1/guides/{self.test_student.pk}/",
    #     )
    #
    # def test_article_verbose_names(self):
    #     self.assertEqual(self.test_student._meta.verbose_name, "student")
    #     self.assertEqual(self.test_student._meta.verbose_name_plural, "students")





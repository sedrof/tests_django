import uuid

from datetime import datetime

from django.test import TestCase

from django.utils import timezone

from guides.models import Guide, LearningProgress, Student, Topic


class LearningProgressTestCase(TestCase):
    @classmethod
    def setUp(cls):

        cls.test_topic = Topic.objects.create(
            title="test_topic_title_for_guide"
        )

        cls.test_guide = Guide.objects.create(
            title="test_guide_title_for_learning_process",
            topic=cls.test_topic
        )

        cls.test_student = Student.objects.create(
            fullName="test_full_name",
            publicName="test_public_name",
            bigCommandId=str(uuid.uuid4())
        )


        cls.now = timezone.now()

        cls.test_learning_process = LearningProgress.objects.create(
            startDate=cls.now,
            lessonsCompleted=1,
            completionDate=cls.now ,
            student=cls.test_student,
            guide=cls.test_guide
        )

    def test_model_fields(self):
        self.assertIsInstance(self.test_learning_process.startDate, datetime)
        self.assertEqual(self.test_learning_process.lessonsCompleted, 1)
        self.assertIsInstance(self.test_learning_process.completionDate, datetime)



    def test_string_representation(self):
        self.assertEqual(str(self.test_learning_process), "test_full_name's learning progress")



    def test_model_absolute_url(self):
        self.assertEqual(
            self.test_learning_process.get_absolute_url(),
            f"/api/v1/guides/{self.test_learning_process.pk}/",
        )

    def test_article_verbose_names(self):
        self.assertEqual(self.test_learning_process._meta.verbose_name, "student")
        self.assertEqual(self.test_learning_process._meta.verbose_name_plural, "students")





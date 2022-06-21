from datetime import datetime
from django.test import TestCase

from django.utils import timezone

from community.models import Category


class PostViewTestCase(TestCase):
    @classmethod
    def setUp(cls):
        cls.now = timezone.now()



        cls.test_category = Category.objects.create(
            title="test_category_title",
            slug="test_category_slug",
            description="test_category_describtion",
            thumbnailURL="https://link.com/",
        )

    def test_model_fields(self):
        self.assertEqual(self.test_category.title, 'test_category_title')
        self.assertEqual(self.test_category.description, 'test_category_describtion')
        self.assertEqual(self.test_category.thumbnailURL, 'https://link.com/')


    def test_string_representation(self):
        self.assertEqual(str(self.test_category), self.test_category.title)



    def test_model_absolute_url(self):
        self.assertEqual(
            self.test_category.get_absolute_url(),
            f"/api/v1/community/categories/{self.test_category.slug}/",
        )

    def test_verbose_names(self):
        self.assertEqual(self.test_category._meta.verbose_name, "category")
        self.assertEqual(self.test_category._meta.verbose_name_plural, "categories")


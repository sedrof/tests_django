
from django.test import TestCase

from guides.models.categories import Category
from includes.common.bigcommand_apps import BigCommandApps

class CategoryTestCase(TestCase):
    @classmethod
    def setUp(cls):

        cls.test_category = Category.objects.create(
            title="test_category_title",
            slug="test_category_slug",
            app=BigCommandApps.Adilo,
            description="test_category_describtion",
            thumbnailURL="https://link.com/",
        )

    def test_model_fields(self):
        self.assertEqual(self.test_category.title, 'test_category_title')
        self.assertEqual(self.test_category.description, 'test_category_describtion')
        self.assertEqual(self.test_category.thumbnailURL, 'https://link.com/')
        self.assertEqual(self.test_category.app, 6)


    def test_string_representation(self):
        self.assertEqual(str(self.test_category), self.test_category.title)

    def save_slug_on_creation(self):
        self.assertEqual(self.test_category.slug, "test_category_title")

    def test_model_absolute_url(self):
        self.assertEqual(
            self.test_category.get_absolute_url(),
            f"/api/v1/guides/categories/{self.test_category.slug}/",
        )

    def test_verbose_names(self):
        self.assertEqual(self.test_category._meta.verbose_name, "category")
        self.assertEqual(self.test_category._meta.verbose_name_plural, "categories")


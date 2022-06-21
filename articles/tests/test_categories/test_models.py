from django.test import TestCase

# from articles.models.categories import Category
from articles.tests.test_member import initialize_category


class CategoryTestCase(TestCase):
    @classmethod
    def setUp(cls):

        cls.test_category = initialize_category()

    def test_model_fields(self):
        self.assertEqual(self.test_category.description, "test_describtion_1")
        self.assertEqual(self.test_category.app, "22")
        self.assertEqual(self.test_category.language, "EN")
        self.assertEqual(self.test_category.title, "test_slug_field")

    def test_model_str(self):
        self.assertEqual(str(self.test_category), "test_slug_field")

    def test_model_is_assigned_slug_on_creation(self):
        self.assertEqual(self.test_category.slug, "test_slug_field")

    def test_model_absolute_url(self):
        self.assertEqual(
            self.test_category.get_absolute_url(),
            f"/api/v1/test_slug_field/{self.test_category.slug}/",
        )

    def test_category_verbose_names(self):
        self.assertEqual(self.test_category._meta.verbose_name, "categories")
        self.assertEqual(self.test_category._meta.verbose_name_plural, "category")

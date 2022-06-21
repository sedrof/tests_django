from django.test import TestCase

# from articles.models.categories import Category
from articles.tests.test_member import initialize_tag
from includes.common.supported_languages import SupportedLanguages


class TagsTestCase(TestCase):
    @classmethod
    def setUp(cls):

        cls.test_tag = initialize_tag("test_tag_name")

    def test_model_fields(self):
        self.assertEqual(self.test_tag.name, "test_tag_name")
        self.assertEqual(str(self.test_tag.language), SupportedLanguages.EN)

    def test_string_representation(self):
        self.assertEqual(str(self.test_tag.name), "test_tag_name")

    # def test_get_absolute_url(self):
    #     self.assertEqual(
    #         self.test_tag.get_absolute_url(),
    #         f"/api/v1/tags/{self.test_tag.name}/"
    #     )

    def test_verbose_names(self):
        verbose_name = self.test_tag._meta.verbose_name
        verbose_name_plural = self.test_tag._meta.verbose_name_plural
        self.assertEqual(verbose_name, "tag")
        self.assertEqual(verbose_name_plural, "tags")

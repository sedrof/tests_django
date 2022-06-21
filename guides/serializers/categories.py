from rest_framework import serializers

from articles.serializers.language_validator import LanguageValidator
from guides.models import Category


class CategorySerializer(LanguageValidator, serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        ref_name = "GuideCategorySerializer"

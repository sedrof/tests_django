from rest_framework import serializers

from articles.models import Category
from articles.serializers.language_validator import LanguageValidator


class CategorySerializer(LanguageValidator, serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

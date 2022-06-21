from rest_framework import serializers

from articles.models import Tag
from articles.serializers.language_validator import LanguageValidator


class TagSerializer(LanguageValidator, serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

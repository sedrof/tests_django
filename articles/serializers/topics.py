from rest_framework import serializers

from articles.models import Topic, Article
from articles.serializers.language_validator import LanguageValidator


class TopicSerializer(LanguageValidator, serializers.ModelSerializer):
    class BasicArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ["id", "title", "slug", "language"]
            ref_name = "BasicArticleSerializerInternal"

    articles = BasicArticleSerializer(read_only=True, many=True)

    class Meta:
        model = Topic
        fields = "__all__"

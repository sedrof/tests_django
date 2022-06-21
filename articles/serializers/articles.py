from rest_framework import serializers

from articles.models import Article, ArticleView
from articles.serializers.language_validator import LanguageValidator
from .categories import CategorySerializer
from .topics import TopicSerializer


class BasicArticleSerializer(LanguageValidator, serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ["isHelpFulCount", "isNotHelpFulCount"]


class ArticleSerializer(BasicArticleSerializer):
    class SimpleArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ["id", "title", "slug"]

    category = CategorySerializer(read_only=True, source="topic.category")
    topic = TopicSerializer(read_only=True)
    relatedArticles = SimpleArticleSerializer(
        read_only=True, many=True, source="related_articles"
    )

    class Meta:
        model = Article
        exclude = ["isHelpFulCount", "isNotHelpFulCount"]


class ArticleViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleView
        fields = "__all__"

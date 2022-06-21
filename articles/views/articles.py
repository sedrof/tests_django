from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from articles.models import Article
from articles.serializers import ArticleSerializer, BasicArticleSerializer
from articles.serializers.language_validator import LanguageValidator


class ArticleViewSet(LanguageValidator, viewsets.ModelViewSet):
    queryset = Article.objects.all()
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action in ["create", "update"]:
            return BasicArticleSerializer
        return ArticleSerializer

    @action(
        detail=False,
        methods=["GET"],
        url_path="trending",
        url_name="trending",
    )
    def get_trending_articles(self, request: Request, **kwargs) -> Response:
        ...

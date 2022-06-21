from rest_framework import viewsets

from articles.models import ArticleView
from articles.serializers import ArticleViewSerializer
from includes.common.client_utils import get_client_ip


class ArticleViewViewSet(viewsets.ModelViewSet):
    queryset = ArticleView.objects.all()
    serializer_class = ArticleViewSerializer

    def perform_create(self, serializer: ArticleViewSerializer):
        serializer.save(ipAddress=get_client_ip(self.request))

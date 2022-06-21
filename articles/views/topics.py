from rest_framework import viewsets

from articles.models import Topic
from articles.serializers import TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_field = "slug"

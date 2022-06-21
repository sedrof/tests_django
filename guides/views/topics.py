from rest_framework import viewsets

from guides.models import Topic
from guides.serializers import TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_field = "slug"

from rest_framework import viewsets

from articles.models import Tag
from articles.serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "name"

    def get_queryset(self):
        print(self.kwargs)
        return super().get_queryset()

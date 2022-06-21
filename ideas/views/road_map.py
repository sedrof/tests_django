from rest_framework import viewsets

from ideas.models import RoadMap
from ideas.serializers import RoadMapSerializer


class RoadMapViewSet(viewsets.ModelViewSet):
    queryset = RoadMap.objects.all()
    serializer_class = RoadMapSerializer

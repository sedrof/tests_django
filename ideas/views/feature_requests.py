from rest_framework import viewsets

from ideas.models import FeatureRequest
from ideas.serializers import FeatureRequestSerializer


class FeatureRequestViewSet(viewsets.ModelViewSet):
    queryset = FeatureRequest.objects.all()
    serializer_class = FeatureRequestSerializer

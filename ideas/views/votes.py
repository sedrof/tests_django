from rest_framework import viewsets

from ideas.models import Vote
from ideas.serializers import VoteSerializer


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

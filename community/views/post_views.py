from rest_framework import viewsets

from community.models import PostView
from community.serializers import PostViewSerializer
from includes.common.client_utils import get_client_ip


class PostViewViewSet(viewsets.ModelViewSet):
    queryset = PostView.objects.all()
    serializer_class = PostViewSerializer

    def perform_create(self, serializer: PostViewSerializer):
        serializer.save(ipAddress=get_client_ip(self.request))

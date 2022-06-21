from rest_framework import viewsets

from articles.models import Member
from articles.serializers import MemberSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

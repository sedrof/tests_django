from rest_framework import serializers

from articles.models import Category
from .topics import TopicSerializer


class HomeContentSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = "__all__"

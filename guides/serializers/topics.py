from rest_framework import serializers

from articles.serializers.language_validator import LanguageValidator
from guides.models import Topic


class TopicSerializer(LanguageValidator, serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"
        ref_name = "GuideTopicSerializer"

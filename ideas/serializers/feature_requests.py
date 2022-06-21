from rest_framework import serializers

from ideas.models import FeatureRequest


class FeatureRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureRequest
        fields = "__all__"

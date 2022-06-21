from rest_framework import serializers

from ideas.models import RoadMap


class RoadMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadMap
        fields = "__all__"

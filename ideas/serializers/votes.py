from rest_framework import serializers

from ideas.models import Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"

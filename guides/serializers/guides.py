from rest_framework import serializers

from guides.models import Guide, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = "__all__"

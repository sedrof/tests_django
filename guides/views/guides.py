from rest_framework import viewsets

from guides.models import Guide, Lesson
from guides.serializers import LessonSerializer, GuideSerializer


class GuideViewSet(viewsets.ModelViewSet):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
    lookup_field = "slug"


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    lookup_field = "slug"

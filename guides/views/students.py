from rest_framework import viewsets

from guides.models import Student
from guides.serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

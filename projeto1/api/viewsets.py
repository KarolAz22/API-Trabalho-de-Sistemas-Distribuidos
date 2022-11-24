from rest_framework import viewsets
from projeto1.api import serializers
from records import models

class MonographViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MonographSerializer
    queryset = models.Monograph.objects.all()

class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AuthorSerializer
    queryset = models.Author.objects.all()

class CoAdvisorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CoAdvisorSerializer
    queryset = models.Co_advisor.objects.all()

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()
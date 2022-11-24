from rest_framework import viewsets
from projeto1.api import serializers
from records import models

class MonographViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MonographSerializer
    queryset = models.Monograph.objects.all()

class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AuthorSerializer
    queryset = models.Author.objects.all()
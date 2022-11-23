from rest_framework import viewsets
from projeto1.api import serializers
from records import models

class RecordsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RecordsSerializer
    queryset = models.Monograph.objects.all()
from rest_framework import serializers
from records import models

class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Monograph
        fields = '__all__'
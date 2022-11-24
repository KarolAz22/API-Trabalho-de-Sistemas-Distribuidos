from rest_framework import serializers
from records import models

class MonographSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Monograph
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = '__all__'
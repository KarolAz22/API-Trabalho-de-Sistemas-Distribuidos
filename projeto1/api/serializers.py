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

class CoAdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Co_advisor
        fields = '__all__'

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Advisor
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'
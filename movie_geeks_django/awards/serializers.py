from rest_framework import serializers
from .models import Award


class BasicAwardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Award
        fields = '__all__'
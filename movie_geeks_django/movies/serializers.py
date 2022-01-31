from rest_framework import serializers
from .models import Film


class BasicFilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = '__all__'

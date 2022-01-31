from rest_framework import serializers
from .models import FilmAward, FilmAwardReceived


class BasicFilmAwardSerializer(serializers.ModelSerializer):

    class Meta:
        model = FilmAward
        fields = '__all__'


class BasicReceivedFilmAwardSerializer(serializers.ModelSerializer):

    class Meta:
        model = FilmAwardReceived
        fields = '__all__'

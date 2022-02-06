from rest_framework import serializers
from .models import Film, Genre


class FilmSerializerForDisplayInFilmographies(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = ['id', 'name', 'year_of_release']


class GenreSerializerForDisplayInFilmInfo(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['id', 'name']

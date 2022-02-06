from rest_framework import serializers
from .models import Film, Genre
from performers.nested_serializers import PerformerSerializerForDisplayInCast
from .nested_serializers import FilmSerializerForDisplayInFilmographies, GenreSerializerForDisplayInFilmInfo


class BasicFilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = '__all__'


class ExtendedFilmSerializer(serializers.ModelSerializer):
    genre = GenreSerializerForDisplayInFilmInfo(many=False, read_only=True)
    director = PerformerSerializerForDisplayInCast(many=False, read_only=True)
    cast = PerformerSerializerForDisplayInCast(many=True, read_only=True)

    class Meta:
        model = Film
        fields = ['id', 'name', 'year_of_release', 'genre', 'synopsis', 'director', 'cast', 'url_name']


class ExtendedGenreSerializer(serializers.ModelSerializer):
    films = FilmSerializerForDisplayInFilmographies(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ['id', 'name', 'description', 'films', 'url_name']


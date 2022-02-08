from rest_framework import serializers
from .models import Film, Genre, FilmReview
from performers.nested_serializers import PerformerSerializerForDisplayInCast
from .nested_serializers import FilmSerializerForDisplayInFilmographies, \
    GenreSerializerForDisplayInFilmInfo, FilmReviewSerializerForDisplayInLists


class BasicFilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = '__all__'


class ExtendedFilmSerializer(serializers.ModelSerializer):
    genre = GenreSerializerForDisplayInFilmInfo(many=False, read_only=True)
    director = PerformerSerializerForDisplayInCast(many=False, read_only=True)
    cast = PerformerSerializerForDisplayInCast(many=True, read_only=True)
    reviews = FilmReviewSerializerForDisplayInLists(many=True, read_only=True)

    class Meta:
        model = Film
        fields = ['id', 'name', 'year_of_release', 'genre', 'synopsis', 'director', 'cast', 'reviews', 'url_name']


class ExtendedGenreSerializer(serializers.ModelSerializer):
    films = FilmSerializerForDisplayInFilmographies(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ['id', 'name', 'description', 'films', 'url_name']


class ExtendedFilmReviewSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.user.username')
    film_reviewed = FilmSerializerForDisplayInFilmographies(many=False, read_only=True)

    class Meta:
        model = FilmReview
        fields = ['id', 'author', 'rating', 'title', 'written_on', 'content', 'film_reviewed']


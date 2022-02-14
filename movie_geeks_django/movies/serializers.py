from rest_framework import serializers

from performers.nested_serializers import PerformerSerializerForDisplayInCast

from .models import Film, FilmReview, Genre
from .nested_serializers import (FilmReviewSerializerForDisplayInLists,
                                 FilmSerializerForDisplayInFilmographies,
                                 GenreSerializerForDisplayInFilmInfo)

# ----------------------------------------- FILM serializers ---------------------------------------------------------#


class BasicFilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        # fields = "__all__"
        fields = ['id', 'name', 'year_of_release', 'genre', 'synopsis', 'director', 'cast']


class ExtendedFilmSerializer(serializers.ModelSerializer):
    genre = GenreSerializerForDisplayInFilmInfo(many=True, read_only=True, required=False)
    director = PerformerSerializerForDisplayInCast(many=True, read_only=True, required=False)
    cast = PerformerSerializerForDisplayInCast(many=True, read_only=True, required=False)
    reviews = FilmReviewSerializerForDisplayInLists(many=True, read_only=True)

    class Meta:
        model = Film
        fields = [
            "id",
            "name",
            "year_of_release",
            "genre",
            "synopsis",
            "director",
            "cast",
            "reviews",
            "url_name",
        ]
# ----------------------------------------- GENRE serializers ---------------------------------------------------------#


class BasicGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ExtendedGenreSerializer(serializers.ModelSerializer):
    films = FilmSerializerForDisplayInFilmographies(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ["id", "name", "films", "url_name"]
# ----------------------------------------- REVIEW serializers --------------------------------------------------------#


class BasicFilmReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmReview
        fields = "__all__"


class ExtendedFilmReviewSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.user.username", allow_blank=True, read_only=True)
    film_reviewed = FilmSerializerForDisplayInFilmographies(many=False, read_only=True)

    class Meta:
        model = FilmReview
        fields = [
            "id",
            "author",
            "rating",
            "title",
            "written_on",
            "content",
            "film_reviewed",
            "url_name"
        ]

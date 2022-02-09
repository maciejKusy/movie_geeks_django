from rest_framework import serializers

from performers.nested_serializers import PerformerSerializerForDisplayInCast

from .models import Film, FilmReview, Genre
from .nested_serializers import (FilmReviewSerializerForDisplayInLists,
                                 FilmSerializerForDisplayInFilmographies,
                                 GenreSerializerForDisplayInFilmInfo)


class BasicFilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = "__all__"


class ExtendedFilmSerializer(serializers.ModelSerializer):
    genre = GenreSerializerForDisplayInFilmInfo(many=False, read_only=True)
    director = PerformerSerializerForDisplayInCast(many=False, read_only=True)
    cast = PerformerSerializerForDisplayInCast(many=True, read_only=True)
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


class BasicGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ExtendedGenreSerializer(serializers.ModelSerializer):
    films = FilmSerializerForDisplayInFilmographies(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ["id", "name", "description", "films", "url_name"]


class BasicFilmReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmReview
        fields = "__all__"


class ExtendedFilmReviewSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.user.username")
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
        ]

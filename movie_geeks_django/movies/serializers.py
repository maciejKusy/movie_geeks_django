from performers.nested_serializers import PerformerSerializerForDisplayInLists
from rest_framework import serializers

from .models import Film, FilmReview, Genre
from .nested_serializers import (FilmReviewSerializerForDisplayInLists,
                                 FilmSerializerForDisplayInFilmographies,
                                 GenreSerializerForDisplayInFilmInfo)

# ----------------------------------------- FILM serializers ---------------------------------------------------------#


class BasicFilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = "__all__"


class ExtendedFilmSerializer(serializers.ModelSerializer):
    """
    Serves to expose extended information to the user. To be edited if additional info is to be exposed to
    a GET response.
    """

    genre = GenreSerializerForDisplayInFilmInfo(many=True, required=False)
    director = PerformerSerializerForDisplayInLists(many=True, required=False)
    cast = PerformerSerializerForDisplayInLists(many=True, required=False)
    reviews = FilmReviewSerializerForDisplayInLists(many=True, read_only=True)
    overall_score = serializers.FloatField(source="get_score")

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
            "overall_score",
            "url_name",
        ]


# ----------------------------------------- GENRE serializers ---------------------------------------------------------#


class BasicGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ExtendedGenreSerializer(serializers.ModelSerializer):
    """
    Serves to expose extended information to the user. To be edited if additional info is to be exposed to
    a GET response.
    """

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
    """
    Serves to expose extended information to the user. To be edited if additional info is to be exposed to
    a GET response.
    """

    author = serializers.CharField(
        source="author.user.username", allow_blank=True, read_only=True
    )
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
            "url_name",
        ]

from rest_framework import serializers

from .models import Film, FilmReview, Genre


class FilmSerializerForDisplayInFilmographies(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ["id", "name", "year_of_release"]


class GenreSerializerForDisplayInFilmInfo(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class FilmReviewSerializerForDisplayInLists(serializers.ModelSerializer):
    class Meta:
        model = FilmReview
        fields = ["id", "title", "rating", "written_on", "content"]

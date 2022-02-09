from rest_framework import serializers

from awards.nested_serializers import \
    ReceivedReceivedAwardSerializerForDisplayInAwardLists
from movies.nested_serializers import FilmSerializerForDisplayInFilmographies

from .models import Performer


class BasicPerformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performer
        fields = "__all__"


class ExtendedPerformerSerializer(serializers.ModelSerializer):
    starred_in = FilmSerializerForDisplayInFilmographies(many=True, read_only=True)
    directed = FilmSerializerForDisplayInFilmographies(many=True, read_only=True)
    awards = ReceivedReceivedAwardSerializerForDisplayInAwardLists(
        many=True, read_only=True
    )

    class Meta:
        model = Performer
        fields = [
            "id",
            "full_name",
            "birthdate",
            "biography",
            "starred_in",
            "directed",
            "awards",
            "url_name",
        ]

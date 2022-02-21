from awards.nested_serializers import \
    ReceivedReceivedAwardSerializerForDisplayInLists
from movies.nested_serializers import FilmSerializerForDisplayInFilmographies
from rest_framework import serializers

from .models import Performer


class BasicPerformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performer
        fields = "__all__"


class ExtendedPerformerSerializer(serializers.ModelSerializer):
    """
    Serves to expose extended information to the user. To be edited if additional info is to be exposed to
    a GET response.
    """

    starred_in = FilmSerializerForDisplayInFilmographies(many=True, read_only=True)
    directed = FilmSerializerForDisplayInFilmographies(many=True, read_only=True)
    awards = ReceivedReceivedAwardSerializerForDisplayInLists(many=True, read_only=True)

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

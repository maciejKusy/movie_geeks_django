from movies.nested_serializers import FilmSerializerForDisplayInFilmographies
from performers.nested_serializers import PerformerSerializerForDisplayInLists
from rest_framework import serializers

from .models import FilmAward, FilmAwardReceived

# --------------------------------------------##GENERAL AWARDS serializers##-------------------------------------------#


class BasicFilmAwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmAward
        fields = "__all__"


class ExtendedFilmAwardSerializer(serializers.ModelSerializer):
    """
    Serves to expose extended information to the user. To be edited if additional info is to be exposed to
    a GET response.
    """

    recipients = serializers.ListField(source="get_all_recipients", required=False)

    class Meta:
        model = FilmAward
        fields = [
            "id",
            "name",
            "date_established",
            "description",
            "recipients",
            "url_name",
        ]


# --------------------------------------------##RECEIVED AWARDS serializers##------------------------------------------#


class BasicReceivedFilmAwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmAwardReceived
        fields = "__all__"


class ExtendedReceivedFilmAwardSerializer(serializers.ModelSerializer):
    """
    Serves to expose extended information to the user. To be edited if additional info is to be exposed to
    a GET response.
    """

    name = serializers.CharField(source="name.name", read_only=True)
    awarded_for = FilmSerializerForDisplayInFilmographies(many=False, read_only=True)
    recipient = PerformerSerializerForDisplayInLists(many=False, read_only=True)

    class Meta:
        model = FilmAwardReceived
        fields = [
            "id",
            "name",
            "awarded_on",
            "award_status",
            "awarded_for",
            "recipient",
            "url_name",
        ]

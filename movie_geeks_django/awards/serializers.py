from rest_framework import serializers

from movies.nested_serializers import FilmSerializerForDisplayInFilmographies
from performers.nested_serializers import PerformerSerializerForDisplayInCast

from .models import FilmAward, FilmAwardReceived

# --------------------------------------------##GENERAL AWARDS serializers##-------------------------------------------#


class BasicFilmAwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmAward
        fields = "__all__"


class ExtendedFilmAwardSerializer(serializers.ModelSerializer):
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
    name = serializers.CharField(source="name.name", read_only=True)
    awarded_for = FilmSerializerForDisplayInFilmographies(many=False, read_only=True)
    recipient = PerformerSerializerForDisplayInCast(many=False, read_only=True)

    class Meta:
        model = FilmAwardReceived
        fields = ["id", "name", "awarded_on", "award_status", "awarded_for", "recipient", "url_name"]

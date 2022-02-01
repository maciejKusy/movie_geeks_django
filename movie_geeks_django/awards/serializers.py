from rest_framework import serializers
from .models import FilmAward, FilmAwardReceived
from movies.nested_serializers import FilmSerializerForDisplayInFilmographies
from performers.nested_serializers import PerformerSerializerForDisplayInCast


# --------------------------------------------##GENERAL AWARDS BELOW##--------------------------------------------#


class BasicFilmAwardSerializer(serializers.ModelSerializer):

    class Meta:
        model = FilmAward
        fields = '__all__'


class ExtendedFilmAwardSerializer(serializers.ModelSerializer):
    recipients = serializers.ListField(source='get_all_recipients')

    class Meta:
        model = FilmAward
        fields = ['id', 'name', 'date_established', 'description', 'recipients']


# --------------------------------------------##RECEIVED AWARDS BELOW##--------------------------------------------#


class BasicReceivedFilmAwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmAwardReceived
        fields = '__all__'


class ExtendedReceivedFilmAwardSerializer(serializers.ModelSerializer):
    awarded_for = FilmSerializerForDisplayInFilmographies(many=False, read_only=True)
    recipient = PerformerSerializerForDisplayInCast(many=False, read_only=True)

    class Meta:
        model = FilmAwardReceived
        fields = ['id', 'type', 'awarded_on', 'awarded_for', 'recipient']

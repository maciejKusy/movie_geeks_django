from rest_framework import serializers
from .models import Performer
from movies.nested_serializers import FilmSerializerForDisplayInFilmographies
from awards.nested_serializers import ReceivedReceivedAwardSerializerForDisplayInAwardLists


class BasicPerformerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Performer
        fields = '__all__'


class ExtendedPerformerSerializer(serializers.ModelSerializer):
    films = FilmSerializerForDisplayInFilmographies(many=True, read_only=True)
    awards = ReceivedReceivedAwardSerializerForDisplayInAwardLists(many=True, read_only=True)

    class Meta:
        model = Performer
        fields = ['id', 'full_name', 'birthdate', 'biography', 'films', 'awards']

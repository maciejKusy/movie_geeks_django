from rest_framework import serializers
from .models import Film
from performers.nested_serializers import PerformerSerializerForDisplayInCast


class BasicFilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = '__all__'


class ExtendedFilmSerializer(serializers.ModelSerializer):
    director = PerformerSerializerForDisplayInCast(many=False, read_only=True)
    cast = PerformerSerializerForDisplayInCast(many=True, read_only=True)

    class Meta:
        model = Film
        fields = ['id', 'name', 'year_of_release', 'synopsis', 'director', 'cast']

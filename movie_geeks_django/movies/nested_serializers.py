from rest_framework import serializers
from .models import Film


class FilmSerializerForDisplayInFilmographies(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = ['id', 'name', 'year_of_release']

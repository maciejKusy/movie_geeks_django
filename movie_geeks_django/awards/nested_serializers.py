from rest_framework import serializers
from .models import FilmAwardReceived


class ReceivedReceivedAwardSerializerForDisplayInAwardLists(serializers.ModelSerializer):

    class Meta:
        model = FilmAwardReceived
        fields = ['id', 'type']

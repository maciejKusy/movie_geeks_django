from rest_framework import serializers

from .models import FilmAwardReceived


class ReceivedReceivedAwardSerializerForDisplayInAwardLists(
    serializers.ModelSerializer
):
    name = serializers.CharField()

    class Meta:
        model = FilmAwardReceived
        fields = ["id", "name"]

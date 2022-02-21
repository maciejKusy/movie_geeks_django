from rest_framework import serializers

from .models import FilmAwardReceived


class ReceivedReceivedAwardSerializerForDisplayInLists(serializers.ModelSerializer):
    """
    Serves to serialize/deserialize the FilmAwardReceived objects for lists of awards - only basic information
    exposed to user.
    """

    name = serializers.CharField()
    awarded_for = serializers.CharField()

    class Meta:
        model = FilmAwardReceived
        fields = ["id", "name", "awarded_for"]

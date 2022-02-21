from rest_framework import serializers

from .models import Performer


class PerformerSerializerForDisplayInLists(serializers.ModelSerializer):
    class Meta:
        model = Performer
        fields = ["id", "full_name"]

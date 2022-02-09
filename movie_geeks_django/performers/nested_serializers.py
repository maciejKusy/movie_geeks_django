from rest_framework import serializers

from .models import Performer


class PerformerSerializerForDisplayInCast(serializers.ModelSerializer):
    class Meta:
        model = Performer
        fields = ["id", "full_name"]

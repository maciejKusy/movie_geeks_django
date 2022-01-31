from rest_framework import serializers
from .models import Performer


class BasicPerformerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Performer
        fields = '__all__'
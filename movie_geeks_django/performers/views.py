from rest_framework.viewsets import ModelViewSet

from movie_geeks_django.mixins import SerializerDifferentiationMixin

from .models import Performer
from .serializers import BasicPerformerSerializer, ExtendedPerformerSerializer


class PerformerView(SerializerDifferentiationMixin, ModelViewSet):
    serializer_class = BasicPerformerSerializer
    queryset = Performer.objects.all()
    lookup_field = "url_name"
    GET_serializer = ExtendedPerformerSerializer
    POST_serializer = BasicPerformerSerializer

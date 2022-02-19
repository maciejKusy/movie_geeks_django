from rest_framework.viewsets import ModelViewSet

from movie_geeks_django.mixins import SerializerDifferentiationMixin

from .models import FilmAward, FilmAwardReceived
from .serializers import (BasicFilmAwardSerializer,
                          BasicReceivedFilmAwardSerializer,
                          ExtendedFilmAwardSerializer,
                          ExtendedReceivedFilmAwardSerializer)


class FilmAwardView(SerializerDifferentiationMixin, ModelViewSet):
    serializer_class = BasicFilmAwardSerializer
    queryset = FilmAward.objects.all()
    lookup_field = "url_name"
    GET_serializer = ExtendedFilmAwardSerializer
    POST_serializer = BasicFilmAwardSerializer


class FilmAwardReceivedView(SerializerDifferentiationMixin, ModelViewSet):
    serializer_class = BasicReceivedFilmAwardSerializer
    queryset = FilmAwardReceived.objects.all()
    lookup_field = "url_name"
    GET_serializer = ExtendedReceivedFilmAwardSerializer
    POST_serializer = BasicReceivedFilmAwardSerializer

from performers.models import Performer
from rest_framework.viewsets import ModelViewSet

from movie_geeks_django.mixins import SerializerDifferentiationMixin

from .models import FilmAward, FilmAwardReceived
from .nested_serializers import \
    ReceivedReceivedAwardSerializerForDisplayInLists
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


class FilmAwardReceivedViewForLists(ModelViewSet):
    """
    Used for the nested performer_router where we want to expose a list of awards received by a given performer.
    """

    serializer_class = ReceivedReceivedAwardSerializerForDisplayInLists

    def get_queryset(self):
        recipient = Performer.objects.all().filter(
            url_name=self.kwargs["performer_url_name"]
        )[0]
        return FilmAwardReceived.objects.all().filter(recipient=recipient)

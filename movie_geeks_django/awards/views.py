from django.http import Http404

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
    lookup_field = "url_name"
    GET_serializer = ExtendedReceivedFilmAwardSerializer
    POST_serializer = BasicReceivedFilmAwardSerializer

    def get_queryset(self):
        award = FilmAward.objects.all().filter(url_name=self.kwargs['filmaward_url_name']).first()
        if not award:
            raise Http404
        awards_received_of_same_type = FilmAwardReceived.objects.all().filter(name=award)
        return awards_received_of_same_type


class FilmAwardReceivedViewForLists(ModelViewSet):
    """
    Used for the nested performer_router where we want to expose a list of awards received by a given performer.
    """

    serializer_class = ReceivedReceivedAwardSerializerForDisplayInLists

    def get_queryset(self):
        recipient = Performer.objects.all().filter(
            url_name=self.kwargs["performer_url_name"]
        ).first()
        if not recipient:
            raise Http404
        return FilmAwardReceived.objects.all().filter(recipient=recipient)

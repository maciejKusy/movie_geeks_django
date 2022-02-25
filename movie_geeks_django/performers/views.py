from django.http import Http404

from awards.models import FilmAward, FilmAwardReceived
from awards.serializers import ExtendedFilmAwardSerializer
from movies.models import Film
from rest_framework.viewsets import ModelViewSet

from movie_geeks_django.mixins import SerializerDifferentiationMixin

from .models import Performer
from .nested_serializers import PerformerSerializerForDisplayInLists
from .serializers import BasicPerformerSerializer, ExtendedPerformerSerializer


class PerformerView(SerializerDifferentiationMixin, ModelViewSet):
    serializer_class = BasicPerformerSerializer
    queryset = Performer.objects.all()
    lookup_field = "url_name"
    GET_serializer = ExtendedPerformerSerializer
    POST_serializer = BasicPerformerSerializer


class PerformerViewForCastLists(ModelViewSet):
    serializer_class = PerformerSerializerForDisplayInLists

    def get_queryset(self):
        film = Film.objects.all().filter(url_name=self.kwargs["film_url_name"]).first()
        if not film:
            raise Http404
        return Performer.objects.all().filter(starred_in=film)


class PerformerViewForRecipientLists(ModelViewSet):
    serializer_class = PerformerSerializerForDisplayInLists

    def get_queryset(self):
        """
        Works slightly differently than other methods for the nested router viewsets.
        1) queries database for the relevant FilmAward model;
        2) queries database for FilmAwardReceived objects of the same type;
        3) iterates over the retrieved FilmAwardsReceived and creates a list of their recipients, effectively creating
        a list of all recipients of a given type of award.
        """
        award = FilmAward.objects.all().filter(url_name=self.kwargs['filmaward_url_name']).first()
        if not award:
            raise Http404
        all_performers = Performer.objects.all().filter(awards__isnull=False, awards__name=award).distinct()
        return all_performers

from awards.models import FilmAward
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
        film = Film.objects.all().filter(url_name=self.kwargs["film_url_name"])[0]
        return Performer.objects.all().filter(starred_in=film)

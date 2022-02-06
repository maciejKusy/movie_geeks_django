from rest_framework.viewsets import ModelViewSet
from .models import FilmAward, FilmAwardReceived
from .serializers import ExtendedFilmAwardSerializer, ExtendedReceivedFilmAwardSerializer


class FilmAwardView(ModelViewSet):
    serializer_class = ExtendedFilmAwardSerializer
    queryset = FilmAward.objects.all()
    lookup_field = 'url_name'


class FilmAwardReceivedView(ModelViewSet):
    serializer_class = ExtendedReceivedFilmAwardSerializer
    queryset = FilmAwardReceived.objects.all()
    lookup_field = 'url_name'

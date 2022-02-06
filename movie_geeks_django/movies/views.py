from rest_framework.viewsets import ModelViewSet
from .models import Film, Genre
from .serializers import ExtendedFilmSerializer, ExtendedGenreSerializer


class FilmView(ModelViewSet):
    serializer_class = ExtendedFilmSerializer
    queryset = Film.objects.all()
    lookup_field = 'url_name'


class GenreView(ModelViewSet):
    serializer_class = ExtendedGenreSerializer
    queryset = Genre.objects.all()
    lookup_field = 'url_name'

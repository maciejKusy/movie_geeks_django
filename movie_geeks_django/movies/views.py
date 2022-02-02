from rest_framework.viewsets import ModelViewSet
from .models import Film
from .serializers import ExtendedFilmSerializer


class FilmView(ModelViewSet):
    serializer_class = ExtendedFilmSerializer
    queryset = Film.objects.all()
    lookup_field = 'url_name'

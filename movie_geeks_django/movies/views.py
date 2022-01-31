from rest_framework.viewsets import ModelViewSet
from .models import Film
from .serializers import BasicFilmSerializer


class FilmView(ModelViewSet):
    serializer_class = BasicFilmSerializer
    queryset = Film.objects.all()

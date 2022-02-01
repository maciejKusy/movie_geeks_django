from rest_framework.viewsets import ModelViewSet
from .models import FilmAward, FilmAwardReceived
from .serializers import BasicFilmAwardSerializer, ExtendedReceivedFilmAwardSerializer


class FilmAwardView(ModelViewSet):
    serializer_class = BasicFilmAwardSerializer
    queryset = FilmAward.objects.all()


class FilmAwardReceivedView(ModelViewSet):
    serializer_class = ExtendedReceivedFilmAwardSerializer
    queryset = FilmAwardReceived.objects.all()

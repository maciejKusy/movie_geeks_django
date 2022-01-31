from rest_framework.viewsets import ModelViewSet
from .models import FilmAward, FilmAwardReceived
from .serializers import BasicFilmAwardSerializer, BasicReceivedFilmAwardSerializer


class FilmAwardView(ModelViewSet):
    serializer_class = BasicFilmAwardSerializer
    queryset = FilmAward.objects.all()


class FilmAwardReceivedView(ModelViewSet):
    serializer_class = BasicReceivedFilmAwardSerializer
    queryset = FilmAwardReceived.objects.all()

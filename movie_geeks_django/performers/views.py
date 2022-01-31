from rest_framework.viewsets import ModelViewSet
from .models import Performer
from .serializers import BasicPerformerSerializer


class FilmView(ModelViewSet):
    serializer_class = BasicPerformerSerializer
    queryset = Performer.objects.all()


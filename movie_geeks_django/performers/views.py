from rest_framework.viewsets import ModelViewSet
from .models import Performer
from .serializers import BasicPerformerSerializer


class PerformerView(ModelViewSet):
    serializer_class = BasicPerformerSerializer
    queryset = Performer.objects.all()


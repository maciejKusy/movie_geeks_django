from rest_framework.viewsets import ModelViewSet
from .models import Performer
from .serializers import ExtendedPerformerSerializer


class PerformerView(ModelViewSet):
    serializer_class = ExtendedPerformerSerializer
    queryset = Performer.objects.all()


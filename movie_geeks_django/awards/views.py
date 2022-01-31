from rest_framework.viewsets import ModelViewSet
from .models import Award
from .serializers import BasicAwardSerializer


class AwardView(ModelViewSet):
    serializer_class = BasicAwardSerializer
    queryset = Award.objects.all()

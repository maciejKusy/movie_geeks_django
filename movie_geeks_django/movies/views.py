from django.db.models import QuerySet
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Film, Genre, FilmReview
from .serializers import ExtendedFilmSerializer, ExtendedGenreSerializer, ExtendedFilmReviewSerializer


class FilmView(ModelViewSet):
    serializer_class = ExtendedFilmSerializer
    queryset = Film.objects.all()
    lookup_field = 'url_name'


class GenreView(ModelViewSet):
    serializer_class = ExtendedGenreSerializer
    queryset = Genre.objects.all()
    lookup_field = 'url_name'


class FilmReviewView(ModelViewSet):
    serializer_class = ExtendedFilmReviewSerializer
    permission_classes = [IsAuthenticated]
    queryset = FilmReview.objects.all()
    lookup_field = 'url_name'


class FilmReviewForUserView(ModelViewSet):
    serializer_class = ExtendedFilmReviewSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'url_name'
    queryset = FilmReview.objects.all()

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = FilmReview.objects.all().filter(author=self.request.user.userprofile)
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset

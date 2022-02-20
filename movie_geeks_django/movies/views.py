from django.db.models import QuerySet
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from movie_geeks_django.mixins import SerializerDifferentiationMixin
from performers.models import Performer
from performers.serializers import BasicPerformerSerializer

from .models import Film, FilmReview, Genre
from .nested_serializers import FilmSerializerForDisplayInFilmographies
from .serializers import (BasicFilmReviewSerializer, BasicFilmSerializer,
                          BasicGenreSerializer, ExtendedFilmReviewSerializer,
                          ExtendedFilmSerializer, ExtendedGenreSerializer)


class FilmView(SerializerDifferentiationMixin, ModelViewSet):
    serializer_class = BasicFilmSerializer
    queryset = Film.objects.all()
    lookup_field = "url_name"
    GET_serializer = ExtendedFilmSerializer
    POST_serializer = BasicFilmSerializer


class FilmViewForDirectedFilmsList(ModelViewSet):
    serializer_class = FilmSerializerForDisplayInFilmographies

    def get_queryset(self):
        director = Performer.objects.all().filter(url_name=self.kwargs['performer_url_name'])[0]
        return Film.objects.all().filter(director=director)


class FilmViewForFilmsStarredInList(ModelViewSet):
    serializer_class = FilmSerializerForDisplayInFilmographies

    def get_queryset(self):
        actor = Performer.objects.all().filter(url_name=self.kwargs['performer_url_name'])[0]
        return Film.objects.all().filter(cast=actor)


class GenreView(SerializerDifferentiationMixin, ModelViewSet):
    serializer_class = BasicGenreSerializer
    queryset = Genre.objects.all()
    lookup_field = "url_name"
    GET_serializer = ExtendedGenreSerializer
    POST_serializer = BasicGenreSerializer


class FilmReviewView(SerializerDifferentiationMixin, ModelViewSet):
    serializer_class = BasicFilmReviewSerializer
    permission_classes = [IsAuthenticated]
    queryset = FilmReview.objects.all()
    lookup_field = "url_name"
    GET_serializer = ExtendedFilmReviewSerializer
    POST_serializer = BasicFilmReviewSerializer


class FilmReviewForUserView(SerializerDifferentiationMixin, ModelViewSet):
    serializer_class = BasicFilmReviewSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "url_name"
    queryset = FilmReview.objects.all()
    GET_serializer = ExtendedFilmReviewSerializer
    POST_serializer = BasicFilmReviewSerializer

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method." % self.__class__.__name__
        )

        queryset = FilmReview.objects.all().filter(author=self.request.user.userprofile)
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.userprofile)

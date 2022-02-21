from django.db.models import QuerySet
from performers.models import Performer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from movie_geeks_django.mixins import SerializerDifferentiationMixin

from .models import Film, FilmReview, Genre
from .nested_serializers import (FilmReviewSerializerForDisplayInLists,
                                 FilmSerializerForDisplayInFilmographies)
from .serializers import (BasicFilmReviewSerializer, BasicFilmSerializer,
                          BasicGenreSerializer, ExtendedFilmReviewSerializer,
                          ExtendedFilmSerializer, ExtendedGenreSerializer)


class FilmView(SerializerDifferentiationMixin, ModelViewSet):
    serializer_class = BasicFilmSerializer
    queryset = Film.objects.all()
    lookup_field = "url_name"
    GET_serializer = ExtendedFilmSerializer
    POST_serializer = BasicFilmSerializer


class FilmsDirectedViewForLists(ModelViewSet):
    serializer_class = FilmSerializerForDisplayInFilmographies

    def get_queryset(self):
        director = Performer.objects.all().filter(
            url_name=self.kwargs["performer_url_name"]
        )[0]
        return Film.objects.all().filter(director=director)


class FilmsStarredInViewForLists(ModelViewSet):
    serializer_class = FilmSerializerForDisplayInFilmographies

    def get_queryset(self):
        actor = Performer.objects.all().filter(
            url_name=self.kwargs["performer_url_name"]
        )[0]
        return Film.objects.all().filter(cast=actor)


class GenreView(SerializerDifferentiationMixin, ModelViewSet):
    serializer_class = BasicGenreSerializer
    queryset = Genre.objects.all()
    lookup_field = "url_name"
    GET_serializer = ExtendedGenreSerializer
    POST_serializer = BasicGenreSerializer


class FilmReviewView(SerializerDifferentiationMixin, ModelViewSet):
    serializer_class = BasicFilmReviewSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = FilmReview.objects.all()
    lookup_field = "url_name"
    GET_serializer = ExtendedFilmReviewSerializer
    POST_serializer = BasicFilmReviewSerializer


class FilmReviewViewForLists(ModelViewSet):
    serializer_class = FilmReviewSerializerForDisplayInLists

    def get_queryset(self):
        film = Film.objects.all().filter(url_name=self.kwargs["film_url_name"])[0]
        return FilmReview.objects.all().filter(film_reviewed=film)


class FilmReviewForUserView(SerializerDifferentiationMixin, ModelViewSet):
    serializer_class = BasicFilmReviewSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "url_name"
    queryset = FilmReview.objects.all()
    GET_serializer = ExtendedFilmReviewSerializer
    POST_serializer = BasicFilmReviewSerializer

    def get_queryset(self):
        """
        Queries the database for film reviews and filters out only ones that are authored by the current session user.
        """
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
        """
        Ensures that the author of a film review (session user) us saved automatically in the model.
        """
        serializer.save(author=self.request.user.userprofile)

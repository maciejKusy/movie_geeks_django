from django.db.models import QuerySet
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Film, FilmReview, Genre
from .serializers import (BasicFilmReviewSerializer, BasicFilmSerializer,
                          BasicGenreSerializer, ExtendedFilmReviewSerializer,
                          ExtendedFilmSerializer, ExtendedGenreSerializer)


class FilmView(ModelViewSet):
    serializer_class = ExtendedFilmSerializer
    queryset = Film.objects.all()
    lookup_field = "url_name"

    def get_serializer_class(self):
        """
        Ensures that the contents of a PUT, POST or PATCH request do not contain the serialized versions of nested
        objects.
        :return: either the no-nested-serialization serializer of the default one depending on request method
        """
        if self.request.method in ["PUT", "POST", "PATCH"]:
            return BasicFilmSerializer
        else:
            return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        """
        Ensures that the response to a POST request is parsed using the elaborate (nested serialization included)
        serialization instead of the one used for the request itself.
        :param request: HTTP request sent by user
        :return: HTTP response from server
        """
        serializer = ExtendedFilmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, *args, **kwargs):
        """
        Ensures that the response to a PUT/PATCH request is parsed using the elaborate (nested serialization included)
        serialization instead of the one used for the request itself.
        :param request: HTTP request sent by user
        :return: HTTP response from server
        """
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return_serializer = ExtendedFilmSerializer(
            instance, data=request.data, partial=partial
        )
        return_serializer.is_valid(raise_exception=True)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(return_serializer.data)


class GenreView(ModelViewSet):
    serializer_class = ExtendedGenreSerializer
    queryset = Genre.objects.all()
    lookup_field = "url_name"

    def get_serializer_class(self):
        """
        Ensures that the contents of a PUT, POST or PATCH request do not contain the serialized versions of nested
        objects.
        :return: either the no-nested-serialization serializer of the default one depending on request method
        """
        if self.request.method in ["PUT", "POST", "PATCH"]:
            return BasicGenreSerializer
        else:
            return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        """
        Ensures that the response to a POST request is parsed using the elaborate (nested serialization included)
        serialization instead of the one used for the request itself.
        :param request: HTTP request sent by user
        :return: HTTP response from server
        """
        serializer = ExtendedGenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, *args, **kwargs):
        """
        Ensures that the response to a PUT/PATCH request is parsed using the elaborate (nested serialization included)
        serialization instead of the one used for the request itself.
        :param request: HTTP request sent by user
        :return: HTTP response from server
        """
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return_serializer = ExtendedGenreSerializer(
            instance, data=request.data, partial=partial
        )
        return_serializer.is_valid(raise_exception=True)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(return_serializer.data)


class FilmReviewView(ModelViewSet):
    serializer_class = ExtendedFilmReviewSerializer
    permission_classes = [IsAuthenticated]
    queryset = FilmReview.objects.all()
    lookup_field = "url_name"


class FilmReviewForUserView(ModelViewSet):
    serializer_class = ExtendedFilmReviewSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "url_name"
    queryset = FilmReview.objects.all()

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

    def get_serializer_class(self):
        """
        Ensures that the contents of a PUT, POST or PATCH request do not contain the serialized versions of nested
        objects.
        :return: either the no-nested-serialization serializer of the default one depending on request method
        """
        if self.request.method in ["PUT", "POST", "PATCH"]:
            return BasicFilmReviewSerializer
        else:
            return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.userprofile)

    def create(self, request, *args, **kwargs):
        """
        Ensures that the response to a POST request is parsed using the elaborate (nested serialization included)
        serialization instead of the one used for the request itself.
        :param request: HTTP request sent by user
        :return: HTTP response from server
        """
        serializer = ExtendedFilmReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, *args, **kwargs):
        """
        Ensures that the response to a PUT/PATCH request is parsed using the elaborate (nested serialization included)
        serialization instead of the one used for the request itself.
        :param request: HTTP request sent by user
        :return: HTTP response from server
        """
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return_serializer = ExtendedFilmReviewSerializer(
            instance, data=request.data, partial=partial
        )
        return_serializer.is_valid(raise_exception=True)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(return_serializer.data)

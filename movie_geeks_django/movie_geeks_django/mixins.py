from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class SerializerDifferentiationMixin(ModelViewSet):
    """
    Provides the viewset classes with an option to use different serializers depending on what HTTP method
    is used for a given request.
    """

    GET_serializer = None
    POST_serializer = None

    def get_serializer_class(self):
        """
        Ensures that the contents of a PUT, POST or PATCH request do not contain the serialized versions of nested
        objects.
        :return: either the no-nested-serialization serializer of the default one depending on request method
        """
        if self.request.method in ["GET"]:
            return self.GET_serializer
        else:
            return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        """
        Ensures that the response to a POST request is parsed using the elaborate (nested serialization included)
        serialization instead of the one used for the request itself.
        :param request: HTTP request sent by user
        :return: HTTP response from server
        """
        serializer = self.POST_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response_serializer = self.GET_serializer(instance=serializer.instance)
        headers = self.get_success_headers(serializer.data)
        return Response(
            response_serializer.data, status=status.HTTP_201_CREATED, headers=headers
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
        return_serializer = self.GET_serializer(
            instance, data=request.data, partial=partial
        )
        return_serializer.is_valid(raise_exception=True)

        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}

        return Response(return_serializer.data)

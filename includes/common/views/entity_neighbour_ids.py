from typing import Callable, Type

from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.db.models import QuerySet, Model
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page, cache_control
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


class EntityNeighbourIdsMixinView:
    get_object: Callable[[], Type[Model]]
    get_queryset: Callable[[], QuerySet]

    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(cache_control(private=True))
    @action(
        detail=True,
        methods=["GET"],
        url_path="neighbour-ids",
        url_name="neighbour-ids",
    )
    def get_neighbour_ids(self, request: Request, **kwargs) -> Response:
        """
        Returns the id of the next and previous entity given a particular object.
        This is required for the frontend for next-previous navigation of entity list.
        """
        target = self.get_object()
        queryset_iter = self.get_queryset().iterator()
        previous_obj = None
        while (current := next(queryset_iter, None)) != target:
            previous_obj = current
        previousId = previous_obj.pk if previous_obj else None
        next_obj = next(queryset_iter, None)
        nextId = next_obj.pk if next_obj else None
        return Response(
            {"previousId": previousId, "nextId": nextId},
            status=status.HTTP_200_OK,
        )

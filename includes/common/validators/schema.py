from typing import Mapping, Callable, Any, NoReturn

from django.utils.translation import gettext as _
from pydantic import ValidationError
from rest_framework import exceptions


def validate_schema(data: Mapping, schema: Callable[[Any], NoReturn]) -> NoReturn:
    try:
        if not isinstance(data, Mapping):
            raise TypeError(_("data must be a mapping type"))
        schema(**data)
    except (TypeError, ValidationError) as e:
        raise exceptions.ValidationError(e.errors())

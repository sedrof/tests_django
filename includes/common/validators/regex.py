import re

from django.core.validators import ValidationError, validate_ipv46_address

DOMAIN_NAME = r"^[a-z0-9]([a-z0-9-]+\.){1,}[a-z0-9]+\Z"


def is_valid_ipv46_address(value: str) -> bool:
    try:
        validate_ipv46_address(value)
        return True
    except ValidationError:
        return False


def is_valid_domain_name(value: str) -> bool:
    return bool(re.match(DOMAIN_NAME, value, re.IGNORECASE))

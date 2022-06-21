import pytz

from django.utils import timezone


class TimezoneMiddleware:
    """
    Middleware to retrieve and activate the request user's preferred timezone on
    the user profile model.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.identity:
            tzname = "UTC"
        else:
            tzname = request.identity.get("timezone")

        timezone.activate(pytz.timezone(tzname))
        return self.get_response(request)

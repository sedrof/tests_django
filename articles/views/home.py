from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from articles.models import Category
from articles.serializers import HomeContentSerializer
from includes.common.bigcommand_apps import BigCommandApps
from includes.common.supported_languages import SupportedLanguages


@api_view(["GET"])
def get_home_content(request: Request, **kwargs) -> Response:
    serializer = HomeContentSerializer(
        Category.objects.filter(
            language=request.query_params.get("language", SupportedLanguages.EN),
            app=request.query_params.get("app", BigCommandApps.BoomFront),
        ),
        many=True,
    )
    return Response(serializer.data)

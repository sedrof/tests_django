"""helpcenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

v1_endpoints = [
    path("home/", include("articles.urls.home")),
    path("members/", include("articles.urls.members")),
    path("articles/", include("articles.urls.articles")),
    path("community/", include("community.urls")),
    path("ideas/", include("ideas.urls.feature_requests")),
    path("road-map/", include("ideas.urls.road_map")),
    path("guides/", include("guides.urls")),
]

schema_view = get_schema_view(
    openapi.Info(
        title="BigCommand Help Center API",
        default_version="v1",
        description="Help Center internal API",
        terms_of_service="https://bigcommand.com/policies/terms/",
        contact=openapi.Contact(email="nnaemeka@bigcommand.com"),
    ),
)

urlpatterns = [
    re_path(r"^api/(?P<version>(v1))/", include(v1_endpoints)),
    path(
        "doc/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

# if settings.DEBUG:
#     import debug_toolbar
#
#     urlpatterns += [
#         path("__debug__/", include(debug_toolbar.urls)),
#     ]

from rest_framework.routers import DefaultRouter

from ideas import views

router = DefaultRouter(trailing_slash=True)
router.register(r"", views.RoadMapViewSet, basename="road-map")

urlpatterns = []

urlpatterns += router.urls

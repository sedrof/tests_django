from rest_framework.routers import DefaultRouter

from articles import views

router = DefaultRouter(trailing_slash=True)
router.register(r"", views.MemberViewSet, basename="member")

urlpatterns = []

urlpatterns += router.urls

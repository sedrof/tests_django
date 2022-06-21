from rest_framework.routers import DefaultRouter

from ideas import views

router = DefaultRouter(trailing_slash=True)
router.register(r"votes", views.VoteViewSet, basename="feature-request-vote")
router.register(r"", views.FeatureRequestViewSet, basename="feature-request")

urlpatterns = []

urlpatterns += router.urls

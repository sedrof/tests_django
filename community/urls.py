from rest_framework.routers import DefaultRouter

from community import views

router = DefaultRouter(trailing_slash=True)
router.register(r"categories", views.CategoryViewSet, basename="community-category")
router.register(r"views", views.PostViewViewSet, basename="community-post-view")
router.register(r"", views.PostViewSet, basename="community-post")

urlpatterns = []

urlpatterns += router.urls

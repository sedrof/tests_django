from rest_framework.routers import DefaultRouter

from articles import views

router = DefaultRouter(trailing_slash=True)
router.register(r"topics", views.TopicViewSet, basename="article-topic")
router.register(r"categories", views.CategoryViewSet, basename="article-category")
router.register(r"tags", views.TagViewSet, basename="article-tag")
router.register(r"views", views.ArticleViewViewSet, basename="article-view")
router.register(r"", views.ArticleViewSet, basename="article")

urlpatterns = []

urlpatterns += router.urls

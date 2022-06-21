from rest_framework.routers import DefaultRouter

from guides import views

router = DefaultRouter(trailing_slash=True)
router.register(r"categories", views.CategoryViewSet, basename="guide-category")
router.register(r"topics", views.TopicViewSet, basename="guide-topic")
router.register(r"lessons", views.LessonViewSet, basename="guide-lesson")
router.register(r"students", views.StudentViewSet, basename="student")
router.register(r"", views.GuideViewSet, basename="guide")

urlpatterns = []

urlpatterns += router.urls

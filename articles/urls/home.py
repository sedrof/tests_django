from django.urls import path

from articles import views

urlpatterns = [path("", views.get_home_content, name="home")]

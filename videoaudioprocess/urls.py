# subtitles_api/urls.py
from django.urls import path
from .views import run_subprocess_view

urlpatterns = [
    path("video/", run_subprocess_view, name="get_subtitles"),
]

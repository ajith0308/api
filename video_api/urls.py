# subtitles_api/urls.py

from django.urls import path
from .views import get_subtitles

urlpatterns = [
    path("subtitles/<str:video_id>/", get_subtitles, name="get_subtitles"),
]

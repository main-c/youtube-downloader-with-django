from django.contrib import admin
from django.urls import path

from core.views import DownloadView

app_name = "core"
urlpatterns = [
    path("download/", DownloadView.as_view(), name='youtube'),
]

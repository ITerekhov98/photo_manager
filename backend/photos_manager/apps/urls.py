from django.urls import path

from .photos.views import PhotosListView


urlpatterns = [
    path('photos/', PhotosListView.as_view())
]
from django.urls import path, include

from .photos.views import PhotosListView, CreatePhotoEntityView, PhotoEntityDetailView


urlpatterns = [
    path('photos/', include('photos_manager.apps.photos.urls')),
]
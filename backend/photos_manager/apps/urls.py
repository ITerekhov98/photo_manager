from django.urls import path

from .photos.views import PhotosListView, CreatePhotoEntityView, PhotoEntityDetailView


urlpatterns = [
    path('photos/', PhotosListView.as_view()),
    path('photos/upload', CreatePhotoEntityView.as_view()),
    path('photos/<uuid:id>/', PhotoEntityDetailView.as_view()),
]
from django.urls import path

from .views import (
    PhotosListView,
    CreatePhotoEntityView,
    PhotoEntityDetailView,
    autocomplete_person_name,
)


urlpatterns = [
    path('', PhotosListView.as_view()),
    path('upload/', CreatePhotoEntityView.as_view()),
    path('<uuid:id>/', PhotoEntityDetailView.as_view()),
    path('<uuid:photo_id>/autocomplete/', autocomplete_person_name)
]

from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .serializers import PhotoListSerializer
from .models import PhotoEntity

class PhotosListView(ListAPIView):
    serializer_class = PhotoListSerializer

    def get_queryset(self):
        queryset = PhotoEntity.objects.all()
        return queryset
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.decorators import api_view
from .serializers import PhotoListSerializer, PhotoSerializer
from .models import PhotoEntity
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework import status

class PhotosListView(ListAPIView):
    serializer_class = PhotoListSerializer

    def get_queryset(self):
        queryset = PhotoEntity.objects.all()
        return queryset




class CreatePhotoEntityView(CreateAPIView):
    parser_classes = [JSONParser, MultiPartParser, FileUploadParser]
    serializer_class = PhotoSerializer

    def post(self, request, *args, **kwargs):
        photo = request.data.get('photo')
        if not photo:
            raise ParseError('Request has no resource file attached.')
        photo = PhotoEntity.objects.create(
            photo=photo
        )
        response = PhotoSerializer(
            photo,
            context={"request": request}    
        ).data
        return Response(response, status=status.HTTP_201_CREATED)

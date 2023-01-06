from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.decorators import api_view
from .serializers import PhotoListSerializer, PhotoSerializer
from .models import PhotoEntity
from ..people.models import Person
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
            photo=photo,
            title=request.data.get('title') or '',
            description=request.data.get('description') or '',
        )
        if persons := request.data.get('persons'):
            persons_names = persons.split(',')
            Person.objects.bulk_create(
                [Person(name=name.strip(), photo=photo) for name in persons_names]
            )
        response = PhotoSerializer(
            photo,
            context={"request": request}    
        ).data
        return Response(response, status=status.HTTP_201_CREATED)

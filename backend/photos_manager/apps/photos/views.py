from datetime import date

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.decorators import api_view
from .serializers import PhotoListSerializer, PhotoSerializer
from .models import PhotoEntity
from ..people.models import Person
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework import status
from .services import add_geolocation
from . import filters

class PhotosListView(ListAPIView):
    serializer_class = PhotoListSerializer

    def get_queryset(self):
        queryset = PhotoEntity.objects.prefetch_related('geolocations', 'persons')
        if raw_date := self.request.query_params.get('date'):
            queryset = filters.filter_by_date(queryset, raw_date)
    
        if address := self.request.query_params.get('address'):
            queryset = filters.filter_by_address(queryset, address)

        if person_name := self.request.query_params.get('person_name'):
            queryset = filters.filter_by_person_name(queryset, person_name)

        latitude = self.request.query_params.get('lat')
        longitude = self.request.query_params.get('lon')
        coordinats = (latitude, longitude)
        if all(coordinats):
            queryset = filters.filter_by_coordinats(queryset, coordinats)

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
        add_geolocation(photo, request)

        response = PhotoSerializer(
            photo,
            context={"request": request}    
        ).data
        return Response(response, status=status.HTTP_201_CREATED)


class PhotoEntityDetailView(RetrieveAPIView):
    queryset = PhotoEntity.objects.all()
    serializer_class = PhotoSerializer
    lookup_field = 'id'
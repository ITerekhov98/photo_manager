from rest_framework import serializers

from ..photos.models import PhotoEntity
from ..geolocations.serializers import GeolocationSerializer

class PhotoListSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = PhotoEntity
        fields = (
            'url',
        )

    def get_url(self, obj):
        request = self.context.get('request')
        url = obj.photo.url
        return request.build_absolute_uri(url)


class PhotoSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    url = serializers.SerializerMethodField()
    persons = serializers.SlugRelatedField(
        slug_field='name',
        many=True,
        read_only=True,
    )
    created_at = serializers.DateTimeField(
        read_only=True,
        format="%Y-%m-%dT%H:%M:%S"
    )
    geolocations = GeolocationSerializer(many=True)

    class Meta:
        model = PhotoEntity
        fields = (
            'id',
            'url',
            'geolocations',
            'persons',
            'title',
            'description',
            'created_at'
        )

    def get_url(self, obj):
        request = self.context.get('request')
        url = obj.photo.url
        return request.build_absolute_uri(url)
from rest_framework import serializers

from ..photos.models import PhotoEntity


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
    created_at = serializers.DateTimeField(
        read_only=True,
        format="%Y-%m-%dT%H:%M:%S"
    )

    class Meta:
        model = PhotoEntity
        fields = (
            'id',
            'url',
            'geolocations',
            'people',
            'title',
            'description',
            'created_at'
        )

    def get_url(self, obj):
        request = self.context.get('request')
        url = obj.photo.url
        return request.build_absolute_uri(url)
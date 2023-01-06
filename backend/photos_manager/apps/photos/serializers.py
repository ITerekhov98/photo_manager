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
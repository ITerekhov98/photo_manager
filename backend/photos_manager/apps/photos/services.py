from ..geolocations.models import Geolocation
from .models import PhotoEntity


def add_geolocation(photo, request):
    address = request.data.get('address', '')
    latitude = request.data.get('latitude')
    longitude = request.data.get('longitude')
    location = None
    if all([latitude, longitude]):
        location, created = Geolocation.objects.get_or_create(
            latitude=latitude,
            longitude=longitude,
            defaults={'address': address}
        )
    elif address:
        location, created = Geolocation.objects.get_or_create(
            address=address
        )
    if location:
        location.photos.add(photo)
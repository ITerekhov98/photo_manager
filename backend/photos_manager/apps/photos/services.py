from django.http import HttpRequest
from rest_framework.exceptions import ParseError

from ..geolocations.models import Geolocation
from .models import PhotoEntity


def add_geolocation(photo: PhotoEntity, request: HttpRequest) -> None:
    address = request.data.get('address', '')
    location = None
    coordinats = (
        request.data.get('latitude'),
        request.data.get('longitude')
    )
    if any(coordinats):
        latitude, longitude = format_coordinats(coordinats)
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


def format_coordinats(coordinats: tuple[float | str]) -> tuple[float]:
    if not coordinats or not all(coordinats) or len(coordinats) != 2:
        raise ParseError('invalid coordinats')
    try:
        coordinats = tuple(float(item) for item in coordinats)
    except ValueError:
        raise ParseError('invalid coordinats')
    return coordinats

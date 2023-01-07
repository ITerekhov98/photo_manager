from datetime import date

from django.db.models import QuerySet
from rest_framework.exceptions import ParseError

from .models import PhotoEntity


def filter_by_date(
        queryset: QuerySet[PhotoEntity],
        raw_date: str) -> QuerySet[PhotoEntity]:
    try:
        photo_date = date.fromisoformat(raw_date)
    except ValueError:
        raise ParseError('invalid date format. Use year-month-day')
    return [
        photo for photo in queryset if photo.created_at == photo_date
    ]


def filter_by_address(
        queryset: QuerySet[PhotoEntity],
        address: str) -> QuerySet[PhotoEntity]:

    return [
        photo for photo in queryset if address
        in photo.geolocations.values_list('address', flat=True)
    ]


def filter_by_person_name(
        queryset: QuerySet[PhotoEntity],
        person_name: str) -> QuerySet[PhotoEntity]:

    return [
        photo for photo in queryset if person_name
        in photo.persons.values_list('name', flat=True)
    ]


def filter_by_coordinats(
        queryset: QuerySet[PhotoEntity],
        coordinats: tuple[str | float]) -> QuerySet[PhotoEntity]:

    if len(coordinats) != 2 or not all(coordinats):
        raise ParseError('invalid coordinats')
    try:
        coordinats = tuple(float(item) for item in coordinats)
    except ValueError:
        raise ParseError('invalid coordinats')
    return [
        photo for photo in queryset if coordinats
        in photo.geolocations.values_list('latitude', 'longitude')
    ]

import uuid

from django.db import models


class PhotoEntity(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    photo = models.ImageField('Фото', upload_to='photos')
    geolocations = models.ManyToManyField(
        'geolocations.Geolocation',
        related_name='photos',
        verbose_name='Локации на фото',
        blank=True,
    )
    title = models.CharField('Название', max_length=50, blank=True)
    description = models.TextField('Описание', blank=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self) -> str:
        return self.title or self.id

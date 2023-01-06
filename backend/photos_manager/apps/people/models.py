from django.db import models

from photos_manager.apps.photos.models import PhotoEntity


class Person(models.Model):
    name = models.CharField('Имя', max_length=100)
    photo = models.ForeignKey(
        PhotoEntity,
        on_delete=models.CASCADE,
        verbose_name='Фото',
        related_name='persons',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Человек на фотографии'
        verbose_name_plural = 'Люди на фотографии'

    def __str__(self) -> str:
        return self.name

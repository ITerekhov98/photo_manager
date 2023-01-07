from django.db import models


class Geolocation(models.Model):
    address = models.CharField('Адрес', max_length=200, blank=True)
    latitude = models.FloatField('Широта', blank=True, null=True)
    longitude = models.FloatField('Долгота', blank=True, null=True)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'
        unique_together = ('latitude', 'longitude',)

    def __str__(self) -> str:
        return self.address if self.address else f'{self.latitude} {self.longitude}'
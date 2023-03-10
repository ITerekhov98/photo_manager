# Generated by Django 4.1.5 on 2023-01-06 14:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geolocations', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoEntity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('photo', models.ImageField(upload_to='photos', verbose_name='Фото')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('geolocations', models.ManyToManyField(to='geolocations.geolocation', verbose_name='Локации на фото')),
                ('people', models.ManyToManyField(to='people.person', verbose_name='Люди на фотографии')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
    ]

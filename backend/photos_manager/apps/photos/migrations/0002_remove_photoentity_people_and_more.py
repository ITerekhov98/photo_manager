# Generated by Django 4.1.5 on 2023-01-06 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geolocations', '0001_initial'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photoentity',
            name='people',
        ),
        migrations.AlterField(
            model_name='photoentity',
            name='geolocations',
            field=models.ManyToManyField(blank=True, to='geolocations.geolocation', verbose_name='Локации на фото'),
        ),
    ]

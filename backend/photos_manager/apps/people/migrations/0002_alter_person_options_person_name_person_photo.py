# Generated by Django 4.1.5 on 2023-01-06 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Человек на фотографии', 'verbose_name_plural': 'Люди на фотографии'},
        ),
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='photos.photoentity', verbose_name='Фото'),
        ),
    ]

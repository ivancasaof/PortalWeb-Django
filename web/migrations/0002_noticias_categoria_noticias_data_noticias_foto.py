# Generated by Django 4.0.4 on 2022-05-29 20:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticias',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='categorias.categoria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='noticias',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='noticias',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/'),
        ),
    ]
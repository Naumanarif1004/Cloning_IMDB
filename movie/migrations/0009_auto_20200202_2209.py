# Generated by Django 3.0.2 on 2020-02-02 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_movie_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='banner',
            field=models.ImageField(blank=True, upload_to='movies_banner'),
        ),
    ]

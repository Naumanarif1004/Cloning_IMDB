# Generated by Django 3.0.2 on 2020-02-02 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_movie_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='banner',
            field=models.ImageField(default='', upload_to='movies_banner'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-11 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='image',
            field=models.ImageField(default='sdfsf', upload_to='gallery'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-14 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_author_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='image',
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=1234, upload_to='book_media'),
            preserve_default=False,
        ),
    ]

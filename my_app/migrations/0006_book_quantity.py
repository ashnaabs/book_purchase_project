# Generated by Django 5.0.6 on 2024-05-19 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_remove_author_image_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.2.16 on 2022-12-09 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20221208_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_file',
            field=models.FileField(upload_to='books/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, default='staticfiles/img/default_book_cover.png', upload_to='books_covers/'),
        ),
    ]

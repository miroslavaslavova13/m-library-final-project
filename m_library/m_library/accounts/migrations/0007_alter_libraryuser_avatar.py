# Generated by Django 3.2.16 on 2022-12-04 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20221203_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libraryuser',
            name='avatar',
            field=models.ImageField(default='staticfiles/img/default.png', upload_to='mediafiles/avatars/'),
        ),
    ]

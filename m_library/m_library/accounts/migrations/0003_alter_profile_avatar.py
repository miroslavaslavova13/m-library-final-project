# Generated by Django 3.2.16 on 2022-12-03 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='staticfiles/default.png', upload_to='mediafiles/avatars'),
        ),
    ]
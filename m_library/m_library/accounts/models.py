from django.contrib.auth.models import AbstractUser
from django.db import models


class LibraryUser(AbstractUser):
    MAX_LEN_NAME = 30

    first_name = models.CharField(max_length=MAX_LEN_NAME, )

    last_name = models.CharField(max_length=MAX_LEN_NAME, )

    email = models.EmailField(unique=True)

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Profile(models.Model):
    user = models.OneToOneField(LibraryUser, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.png', upload_to='mediafiles/avatars')

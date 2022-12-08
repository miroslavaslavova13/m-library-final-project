from django.contrib.auth.models import AbstractUser
from django.db import models

from m_library.core.validators import validate_only_letters


class LibraryUser(AbstractUser):
    MAX_LEN_NAME = 30

    first_name = models.CharField(max_length=MAX_LEN_NAME, validators=(validate_only_letters,))

    last_name = models.CharField(max_length=MAX_LEN_NAME, validators=(validate_only_letters, ))

    email = models.EmailField(unique=True)

    avatar = models.ImageField(default='staticfiles/img/default.png', upload_to='avatars/')

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models import RESTRICT

from m_library.core.validators import validate_only_letters

UserModel = get_user_model()


class Book(models.Model):
    MAX_TITLE_LEN = 100
    MAX_AUTHOR_NAME_LEN = 100
    MAX_LANGUAGE_LEN = 20
    MAX_GENRE_LEN = 30

    title = models.CharField(max_length=MAX_TITLE_LEN, null=False, blank=False)

    author = models.CharField(max_length=MAX_AUTHOR_NAME_LEN, validators=(validate_only_letters,), null=False,
                              blank=False)

    cover = models.ImageField(upload_to='books_covers/', null=True, blank=True)

    language = models.CharField(max_length=MAX_LANGUAGE_LEN, validators=(validate_only_letters,), null=False,
                                blank=False)

    genre = models.CharField(max_length=MAX_GENRE_LEN, validators=(validate_only_letters,), null=False, blank=False)

    book_file = models.FileField(upload_to='books/', null=False, blank=False, validators=(FileExtensionValidator(['pdf', 'epub']),),)

    description = models.TextField(null=False, blank=False)

    date_of_publication = models.DateField(auto_now=True, null=False, blank=True)

    user = models.ForeignKey(UserModel, on_delete=RESTRICT)


class BookFavourite(models.Model):
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=False, blank=True)

    user = models.ForeignKey(UserModel, on_delete=RESTRICT)

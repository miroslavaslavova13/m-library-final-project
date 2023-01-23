from django.core.exceptions import ValidationError
from django.test import TestCase

from m_library.accounts.models import LibraryUser


class LibraryUserTests(TestCase):
    def test_user_save_when_first_name_has_only_letters_expect_correct_result(self):
        user = LibraryUser(
            username='miroslava328',
            password='@SlavovaSlavova',
            first_name='Miroslava',
            last_name='Slavova',
            email='miroslava@abv.bg',
        )

        user.full_clean()  # call this for validation
        user.save()

        self.assertIsNotNone(user.pk)

    def test_user_save_when_first_name_does_not_have_only_letters_expect_exception(self):
        user = LibraryUser(
            username='miroslava328',
            password='@SlavovaSlavova',
            first_name='',
            last_name='Slavova',
            email='miroslava@abv.bg',
        )

        with self.assertRaises(ValidationError) as context:
            user.full_clean()
            user.save()

        self.assertIsNotNone(context.exception)


    def test_user_save_when_last_name_has_only_letters_expect_correct_result(self):
        user = LibraryUser(
            username='miroslava328',
            password='@SlavovaSlavova',
            first_name='Miroslava',
            last_name='Slavova',
            email='miroslava@abv.bg',
        )

        user.full_clean()  # call this for validation
        user.save()

        self.assertIsNotNone(user.pk)

    def test_user_save_when_last_name_does_not_have_only_letters_expect_exception(self):
        user = LibraryUser(
            username='miroslava328',
            password='@SlavovaSlavova',
            first_name='Miroslava',
            last_name='',
            email='miroslava@abv.bg',
        )

        with self.assertRaises(ValidationError) as context:
            user.full_clean()
            user.save()

        self.assertIsNotNone(context.exception)

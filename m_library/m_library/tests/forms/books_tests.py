from django.contrib.auth import get_user_model
from django.test import TestCase

from m_library.books.forms import BookDeleteForm
from m_library.books.models import Book

UserModel = get_user_model()


class BookDeleteFormTests(TestCase):
    def test_books_delete_form_fields_are_disabled(self):
        form = BookDeleteForm()
        disabled_fields = {name: field.widget.attrs['readonly'] for name, field in form.fields.items()}

        self.assertEqual('readonly', disabled_fields['title'])
        self.assertEqual('readonly', disabled_fields['author'])
        self.assertEqual('readonly', disabled_fields['cover'])
        self.assertEqual('readonly', disabled_fields['language'])
        self.assertEqual('readonly', disabled_fields['genre'])
        self.assertEqual('readonly', disabled_fields['book_file'])
        self.assertEqual('readonly', disabled_fields['description'])

    def test_books_delete_form_save_method_deletes_the_book_successfully(self):
        credentials = {
            'username': 'some_username123',
            'password': '@SomePassword123'
        }
        user = UserModel.objects.create(**credentials)

        book = Book.objects.create(
            title='Some title',
            author='Some author',
            language='English',
            genre='Genre',
            book_file='some_book.pdf',
            description='Short description of the book',
            user=user
        )

        form = BookDeleteForm(instance=book)
        form.save()

        self.assertNotIn(book, Book.objects.all())
        self.assertEqual(0, len(Book.objects.all()))

from django.test import TestCase

from m_library.books.forms import BookDeleteForm


class BookDeleteFormTests(TestCase):
    def test_blog_post_delete_form_fields_are_disabled(self):
        form = BookDeleteForm()
        disabled_fields = {name:  field.widget.attrs['readonly'] for name, field in form.fields.items()}

        print(disabled_fields)
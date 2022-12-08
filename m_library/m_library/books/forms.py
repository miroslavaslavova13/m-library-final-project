from django import forms

from m_library.books.models import Book, BookFavourite
from m_library.core.form_mixin import DisabledFormMixin


class BookBaseForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('date_of_publication', 'user')


class BookCreateForm(BookBaseForm):
    pass


class BookEditForm(BookBaseForm):
    class Meta:
        model = Book
        exclude = ('book_file', 'date_of_publication', 'user')


class BookDeleteForm(DisabledFormMixin, BookBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            BookFavourite.objects.filter(book_id=self.instance.id).delete()
            self.instance.delete()

        return self.instance


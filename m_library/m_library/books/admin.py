from django.contrib import admin

from m_library.books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)

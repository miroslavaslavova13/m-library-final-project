from django.urls import path, include

from m_library.books.views import library, book_details, add_book, edit_book, delete_book

urlpatterns = [
    path('', library, name='library'),
    path('<int:pk>/', include([
        path('', book_details, name='book details'),
        path('add/', add_book, name='add book'),
        path('edit/', edit_book, name='edit book'),
        path('delete/', delete_book, name='delete book'),
    ]))
]
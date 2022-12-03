from django.urls import path, include

from m_library.books.views import book_details, add_book, edit_book, delete_book, all_books, add_book_to_favourites

urlpatterns = [
    path('', all_books, name='all books'),
    path('add-to-favourites/<int:book_id>/', add_book_to_favourites, name='add to favourites'),
    path('<int:pk>/', include([
        path('', book_details, name='book details'),
        path('add/', add_book, name='add book'),
        path('edit/', edit_book, name='edit book'),
        path('delete/', delete_book, name='delete book'),
    ]))
]
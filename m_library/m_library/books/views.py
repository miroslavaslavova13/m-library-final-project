from django.shortcuts import render, redirect


def all_books(request):
    return render(request, 'books/all-books.html')


def add_book_to_favourites(request):
    return redirect('home')


def book_details(request, pk):
    return render(request, 'books/book-details.html')


def add_book(request):
    return render(request, 'books/add-book.html')


def edit_book(request, pk):
    return render(request, 'books/edit-book.html')


def delete_book(request, pk):
    return render(request, 'books/delete-book.html')

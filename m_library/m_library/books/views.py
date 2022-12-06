from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from m_library.books.forms import BookCreateForm, BookEditForm, BookDeleteForm
from m_library.books.models import Book
from m_library.core.utils import is_owner


def all_books(request):
    books = Book.objects.all()

    context = {
        'books': books
    }
    return render(request, 'books/all-books.html', context)


def add_book_to_favourites(request):
    return redirect('home')


def book_details(request, pk):
    book = Book.objects.filter(pk=pk).get()

    context = {
        'book': book,
        'is_owner': request.user == book.user
    }
    return render(request, 'books/book-details.html', context)


@login_required
def add_book(request):
    if request.method == "GET":
        form = BookCreateForm()
    else:
        form = BookCreateForm(request.POST, request.FILES, initial={'user': request.user})
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('book details', pk=book.pk)

    context = {
        'form': form
    }
    return render(request, 'books/add-book.html', context)


@login_required
def edit_book(request, pk):
    book = Book.objects.filter(pk=pk).get()

    if not is_owner(request, book):
        return redirect('book details', pk=pk)

    if request.method == 'GET':
        form = BookEditForm(instance=book)
    else:
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book details', pk=pk)

    context = {
        'form': form,
        'pk': pk
    }

    return render(request, 'books/edit-book.html', context)


def delete_book(request, pk):
    book = Book.objects.filter(pk=pk).get()

    if not is_owner(request, book):
        return redirect('book details', pk=pk)

    if request.method == 'GET':
        form = BookDeleteForm(instance=book)
    else:
        form = BookDeleteForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('all books')

    context = {
        'form': form,
        'pk': pk
    }

    return render(request, 'books/delete-book.html', context)

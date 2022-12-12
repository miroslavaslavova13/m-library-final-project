from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from m_library.books.forms import BookCreateForm, BookEditForm, BookDeleteForm
from m_library.books.models import Book, BookFavourite
from m_library.common.forms import SearchForm
from m_library.core.utils import is_owner


def all_books(request):
    books = Book.objects.all().order_by('-date_of_publication')
    search_form = SearchForm(request.GET)
    search_pattern = None

    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['text']

    if search_pattern:
        books = books.filter(
            Q(title__icontains=search_pattern) |
            Q(author__icontains=search_pattern))

    context = {
        'books': books,
        'search_form': search_form
    }
    return render(request, 'books/all-books.html', context)


@login_required
def add_book_to_favourites(request, book_id):
    user_added_to_favourites = BookFavourite.objects.filter(book_id=book_id, user_id=request.user.pk)

    if user_added_to_favourites:
        user_added_to_favourites.delete()
    else:
        BookFavourite.objects.create(book_id=book_id, user_id=request.user.pk)

    return redirect(request.META['HTTP_REFERER'] + f'#book-{book_id}')


def book_details(request, pk):
    book = Book.objects.filter(pk=pk).get()
    book.is_favourite = BookFavourite.objects.filter(book_id=pk, user_id=request.user.pk).count() > 0
    print(book.book_file)

    context = {
        'book': book,
        'is_owner': request.user == book.user,
        'recent_books': Book.objects.all()[::-1][:4]
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


@login_required
def delete_book(request, pk):
    book = Book.objects.filter(pk=pk).get()

    if not is_owner(request, book):
        return redirect('book details', pk=pk)

    if request.method == 'GET':
        form = BookDeleteForm(instance=book)
    else:
        form = BookDeleteForm(request.POST or None, instance=book)
        if form.is_valid():
            form.save()
            return redirect('all books')

    context = {
        'form': form,
        'pk': pk
    }

    return render(request, 'books/delete-book.html', context)

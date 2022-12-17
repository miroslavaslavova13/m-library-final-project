from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

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
    try:
        book = get_object_or_404(Book, pk=book_id)
        user_added_to_favourites = BookFavourite.objects.filter(book_id=book.pk, user_id=request.user.pk)

        if user_added_to_favourites:
            user_added_to_favourites.delete()
        else:
            BookFavourite.objects.create(book_id=book_id, user_id=request.user.pk)

        return redirect('book details', pk=book_id)
    except KeyError:
        # TODO change the status code to 404
        return render(request, '404.html')


def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.is_favourite = BookFavourite.objects.filter(book_id=pk, user_id=request.user.pk).count() > 0



    context = {
        'book': book,
        'is_owner': request.user == book.user,
        'is_staff': request.user.is_staff,
        'is_superuser': request.user.is_superuser,
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
    book = get_object_or_404(Book, pk=pk)

    if request.user.is_superuser or request.user.is_staff or is_owner(request, book):

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

    else:
        return redirect('book details', pk=pk)


@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.user.is_superuser or is_owner(request, book):

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

    else:
        return redirect('book details', pk=pk)


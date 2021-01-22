from django.shortcuts import render, redirect
from .models import Book, Author
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import admin
from .forms import BookForm


def all_books(request):
    books = list(Book.objects.all())
    return render(request, 'book/all_books.html', {'title': "All books", "books": books})


def ad(request):
    return render(request, admin.site.urls)


def all_books_by_name(request):
    books = list(Book.objects.all())

    return render(request, 'book/all_books_by_name.html', {'title': "All books by name", "books": books})


def book_by_id(request, id=0):
    book_by_id = Book.objects.get(id=id)
    return render(request, 'book/book_by_id.html', {'title': "Book by id", "book_by_id": book_by_id})


def test(request):
    books = list(Book.objects.all())
    return render(request, 'book/book_plus.html', {'title': "All books", "books": books})


def book_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = BookForm()
        else:
            book = Book.objects.get(id=id)
            form = BookForm(instance=book)
        return render(request, 'book/book_form.html', {'form': form})
    else:
        if id == 0:
            form = BookForm(request.POST)
        else:
            book = Book.objects.get(id=id)
            form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('books')


def book_delete(request, id=0):
    book = Book.objects.get(id=id)
    book.delete()
    # Book.save()
    books = list(Book.objects.all())
    return render(request, 'book/all_books.html', {'title': "All books", "books": books})

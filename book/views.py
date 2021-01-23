from django.shortcuts import render, redirect
from .models import Book, Author
from django.contrib import admin
from .forms import BookForm
from rest_framework import viewsets, generics, permissions
from .serializers import BookSerializer, BookDetailSerializer, BookListSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication



class BookCreateView(generics.CreateAPIView):
    serializer_class = BookDetailSerializer

class BookListView(generics.ListAPIView):
    serializer_class = BookListSerializer
    queryset = Book.objects.all()
    permission_classes = (IsAdminUser, IsAuthenticated, )

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


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

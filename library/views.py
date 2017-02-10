from django.shortcuts import render_to_response
from library.models import Author, Book


def library(request):
    books = Book.objects.all()
    return render_to_response('library.html', {'books': books, })


def book(request, book_id):
    book = Book.objects.get(id=book_id)
    return render_to_response('book.html', {'book': book})


def authors(request):
    authors = Author.objects.all()
    return render_to_response('authors.html', {'authors': authors})


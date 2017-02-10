from django.shortcuts import render_to_response
from library.models import Author, Book


# def library(request):
#     books = Book.objects.all()
#     return render_to_response('main.html', {'books': books, })


def library(request):
    books = Book.objects.all()
    return render_to_response('library.html', {'books': books, })


def book(request, book_id):
    book = Book.objects.get(id=book_id)
    return render_to_response('book.html', {'book': book})

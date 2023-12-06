from django.shortcuts import render

from app.models import Book


def book_list(request):
    books = Book.objects.all()
    context = {"books_list": books}
    return render(request, 'index.html', context=context)
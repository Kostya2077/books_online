from django.shortcuts import render
from .models import Book

def index(request):
    authors = {}
    for book in Book.objects.all():
        author = str(book.author)
        if author not in authors:
            authors[author] = []
        authors[author].append(book.name)

    return render(request, "books_app/index.html", {"authors": authors})

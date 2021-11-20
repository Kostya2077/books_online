from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Book
from .serializer import BookSerializer


""" Вовод списка книг и их авторов """
def index(request):
    authors = {}
    for book in Book.objects.all():
        author = str(book.author)
        if author not in authors:
            authors[author] = []
        authors[author].append(book.name)

    return render(request, "books_app/index.html", {"authors": authors})


""" GET запрос на получение списка всех книг и их авторов """
@api_view(['GET',])
def get_books_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


""" GET запрос на получение содержимого книги по id """
@api_view(['GET'])
def get_book_by_id(request, pk):

    try:
        book = Book.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book)
    return Response(serializer.data)


""" DELETE запрос на удаление книги по id """
@api_view(["DELETE", ])
def delete_book_by_id(request, pk):
    try:
        book = Book.objects.get(id=pk)
        book.delete()
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


""" POST запрос на обновление книги по id """
@api_view(['POST',])
def update_book(request):
    if request.data.get('id', None):
        data = request.data

        try:
            book = Book.objects.get(id=data['id'])
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book, data=data)
        if serializer.is_valid():
            serializer.save()
            book.save()
            return Response(status=status.HTTP_205_RESET_CONTENT)

    return Response(status=status.HTTP_400_BAD_REQUEST)
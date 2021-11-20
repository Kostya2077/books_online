from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('api/v1/books/list', get_books_list),
    path('api/v1/books/<int:pk>', get_book_by_id),
    path('api/v1/books/update', update_book),
    path('api/v1/books/delete/<int:pk>', delete_book_by_id),
]
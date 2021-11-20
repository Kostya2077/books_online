from django.contrib import admin
from .models import *


""" Регистрация модели Author в панель админа """
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "count_books"]
    list_display_links = ["name"]
    search_fields = ["count_books"]


""" Регистрация модели Book в панель админа """
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "author"]
    list_display_links = ["id", "name", "author"]
    search_fields = ["author__name"]


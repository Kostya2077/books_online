from django.contrib import admin
from .models import *


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "count_books")
    list_display_links = ("id", "name")
    search_fields = ["count_books"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "author")
    list_display_links = ("id", "name", "author")
    search_fields = ("author__name",)


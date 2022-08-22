from django.contrib import admin
from book.models import Books, Author


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['name', 'author']


class BookInlineAdmin(admin.StackedInline):
    model = Books
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInlineAdmin]
    list_display = ['author']


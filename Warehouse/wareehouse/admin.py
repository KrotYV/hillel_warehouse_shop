from django.contrib import admin

from .models import Author, Book, BookInstance, Genre, PublishingOffice


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ['name']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    fields = ['name']
    search_fields = ['name']


class BooksInstanceInlineModelAdmin(admin.TabularInline):
    model = BookInstance
    extra = 0


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'rating']
    filter_horizontal = ['author', 'genre']
    list_filter = ['rating', 'author', 'genre']
    inlines = [BooksInstanceInlineModelAdmin]


@admin.register(PublishingOffice)
class PublishingOfficeAdmin(admin.ModelAdmin):
    list_display = ['name', 'pub_year']
    search_fields = ['name']

from django.contrib import admin
from library.models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    filter_horizontal = ('authors',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)

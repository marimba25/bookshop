from django.contrib import admin

# Register your models here.

from .models import Book, Author, Country, BookCategory

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Country)
admin.site.register(BookCategory)




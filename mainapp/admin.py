from django.contrib import admin

# Register your models here.

from .models import Book, Author, Country
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Country)



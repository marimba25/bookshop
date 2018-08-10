from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import Book, Author, Country, BookCategory
from . import models
import random


# Create your views here.

def get_basket(request):
    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    return basket


def main(request):
    books = Book.objects.all()
    basket = get_basket(request)
    context = {'books': books, 'basket': basket}
    return render(request, 'mainapp/index.html', context)


def chunk_data(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def catalog(request, pk=None):
    categories = BookCategory.objects.all()
    basket = get_basket(request)
    context = {'categories': categories, 'basket': basket}

    if pk is None:
        products = Book.objects.all()
    else:
        category_object = get_object_or_404(models.BookCategory, pk=pk)
        products = Book.objects.filter(category=category_object)

    rows_of_products = chunk_data(products, 4)
    context['rows_of_products'] = rows_of_products
    template = 'mainapp/catalog.html'
    return render(request, template, context)


def book(request, pk=None):
    book_obj = get_object_or_404(models.Book, pk=pk)
    basket = get_basket(request)
    template = 'mainapp/book.html'
    context = {'book': book_obj, 'basket': basket}
    return render(request, template, context)


def contacts(request):
    books = Book.objects.all()
    basket = get_basket(request)
    context = {'books': books, 'basket': basket}
    return render(request, 'mainapp/contacts.html', context)


def get_hot_product():
    products = Book.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Book.objects.filter(category=hot_product.category). \
                        exclude(pk=hot_product.pk)[:3]
    return same_products

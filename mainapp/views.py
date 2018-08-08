from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import Book, Author, Country, BookCategory
from . import models


# Create your views here.

def get_basket_context(request):
    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    return {'basket': basket}


def main(request):
    context = {}
    context['books'] = Basket.objects.all()
    context.update(get_basket_context(request))
    return render(request, 'mainapp/index.html', context)


def chunk_data(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def catalog(request, pk=None):
    context = {}
    context['categories'] = BookCategory.objects.all()
    context.update(get_basket_context(request))

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
    context = {}
    book_obj = get_object_or_404(models.Book, pk=pk)
    context['book'] = book_obj
    context.update(get_basket_context(request))
    template = 'mainapp/book.html'
    return render(request, template, context)


def contacts(request):
    context = {}
    context['books'] = Basket.objects.all()
    context.update(get_basket_context(request))
    return render(request, 'mainapp/contacts.html', context)

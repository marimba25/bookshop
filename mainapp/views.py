from django.shortcuts import render, get_object_or_404
from .models import Book, Author, Country, BookCategory
from . import models


# Create your views here.

def main(request):
    return render(request, 'mainapp/index.html', {"username": "marina"})


def chunk_data(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def catalog(request, pk=None):
    print(pk)
    context = {}
    context['categories'] = BookCategory.objects.all()

    if pk is None:
        products = Book.objects.all()
    else:
        category_object = get_object_or_404(models.BookCategory, pk=pk)
        products = Book.objects.filter(category=category_object)

    rows_of_products = chunk_data(products, 4)
    context['rows_of_products'] = rows_of_products
    template = 'mainapp/catalog.html'
    return render(request, template, context)


def contacts(request):
    return render(request, 'mainapp/contacts.html')


def amclassic(request):
    return render(request, 'mainapp/amclassic.html')


def rusclassic(request):
    return render(request, 'mainapp/rusclassic.html')


def capitan(request):
    return render(request, 'mainapp/capitan.html')


def kill(request):
    return render(request, 'mainapp/kill.html')


def mice(request):
    return render(request, 'mainapp/mice.html')


def nadprop(request):
    return render(request, 'mainapp/nadprop.html')


def prest_nakaz(request):
    return render(request, 'mainapp/prest_nakaz.html')


def voyna_i_mir(request):
    return render(request, 'mainapp/voyna_i_mir.html')

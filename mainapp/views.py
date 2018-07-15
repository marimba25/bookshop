from django.shortcuts import render
from .models import Book, Author, Country


# Create your views here.

def main(request):
    return render(request, 'mainapp/index.html', {"username": "marina"})


def catalog(request):

    def chunk_data(data, chunk_size):
        for i in range(0, len(data), chunk_size):
            yield data[i:i + chunk_size]

    title = 'Каталог'
    products = Book.objects.all()
    rows_of_products = chunk_data(products, 4)

    content = {'title': title, 'rows_of_products': rows_of_products}

    return render(request, 'mainapp/catalog.html', content)


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

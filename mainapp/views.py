from django.shortcuts import render


# Create your views here.

def main(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    return render(request, 'mainapp/catalog.html')


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


def voina_i_mir(request):
    return render(request, 'mainapp/voina_i_mir.html')

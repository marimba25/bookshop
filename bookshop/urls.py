"""bookshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
import mainapp.views as mainapp

urlpatterns = [
    url(r'^$', mainapp.main, name='main'),
    url(r'^catalog/', mainapp.catalog, name='catalog'),
    url(r'^contacts/', mainapp.contacts, name='contacts'),
    url(r'^admin/', admin.site.urls),
    url(r'^amclassic/', mainapp.amclassic),
    url(r'^rusclassic/', mainapp.rusclassic),
    url(r'^capitan/', mainapp.capitan),
    url(r'^kill', mainapp.kill),
    url(r'^mice', mainapp.mice),
    url(r'^nadprop', mainapp.nadprop),
    url(r'^prest_nakaz', mainapp.prest_nakaz),
    url(r'^voina_i_mir', mainapp.voina_i_mir)
]

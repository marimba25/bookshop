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
from django.conf.urls import url
import mainapp.views as mainapp
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path

urlpatterns = [
    url(r'^$', mainapp.main, name='main'),
    path('catalog/<int:pk>', mainapp.catalog, name='catalog-list'),
    path('book/<int:pk>', mainapp.book, name='book'),
    path('catalog/', mainapp.catalog, name='catalog'),
    re_path(r'^contacts/', mainapp.contacts, name='contacts'),
    re_path(r'^auth/', include('authapp.urls', namespace='auth')),
    re_path(r'^basket/', include(('basketapp.urls', 'basketapp'), namespace='basket')),
    re_path(r'^adminka/', include(('adminapp.urls', 'adminapp'), namespace='adminka')),
    url(r'^admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
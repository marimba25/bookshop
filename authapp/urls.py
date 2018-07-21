from django.conf.urls import url
import authapp.views as authapp


urlpatterns = [
    url(r'^login/$', authapp.login, name='login'),
    url(r'^logout/$', authapp.logout, name='logout'),
]
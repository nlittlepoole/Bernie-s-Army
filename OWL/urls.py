from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'home', views.index, name='index'),
    url(r'signup', views.signup, name='signup'),
    url(r'activate', views.activate, name='activate'),
]
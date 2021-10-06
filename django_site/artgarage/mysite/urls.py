from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('goods', views.goods, name='goods'),
    path('blog', views.blog, name='blog'),
    path('contacts', views.contacts, name='contacts'),
]
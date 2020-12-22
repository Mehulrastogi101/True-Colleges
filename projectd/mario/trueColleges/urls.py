from django.urls import path

from . import views

urlpatterns = [
    path('', views.font, name='font'),
    path('index', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('search', views.search, name='search'),


]

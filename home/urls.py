
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from . import views
from .views import *
urlpatterns = [
    path('',views.home_view,name='home'),
    path('menu/',views.menu_list,name='menu'),
    path('menu/<slug:slug>/', views.menu_items, name='menu_category'),
]
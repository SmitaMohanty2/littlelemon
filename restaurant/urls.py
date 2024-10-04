from django.contrib import admin
from django.urls import path
from .views import sayHello, index
from . import views

urlpatterns = [
    path('sayhello', sayHello, name='sayHello'),
    path('', index, name='index')
]

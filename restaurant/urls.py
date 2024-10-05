from django.contrib import admin
from django.urls import path
from .views import sayHello, index
from . import views

urlpatterns = [
    path('sayhello', sayHello, name='sayHello'),
    path('', index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]

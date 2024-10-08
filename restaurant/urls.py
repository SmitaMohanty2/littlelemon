from django.contrib import admin
from django.urls import path
from .views import sayHello, index
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import TemplateView

urlpatterns = [
    path('sayhello', sayHello, name='sayHello'),
    path('', index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('',TemplateView.as_view(template_name='index.html'), name='indexpage'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Appsin'),
    path('about/', views.about, name='About'),
    path('service/', views.service, name='Service'),
    path('contact/', views.contact, name='Contact'),
    path('search/', views.search, name='Search'),
]
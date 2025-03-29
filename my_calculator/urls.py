from django.urls import path
from . import views

urlpatterns = [
    # Define your URL patterns here
    # Example:
    # path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path('calculate/', views.calculate, name='calculate'),
]
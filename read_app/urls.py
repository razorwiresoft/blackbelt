from django.urls import path
from . import views

urlpatterns = [
    path(''),
    path('register'),
    path('login'),
    path('books'),
    path('books/new'),
    path('books/create'),
    path('books/<int:id>'),
    path('books/<int:id>/delete'),
    path('books/<int:id>/review'),
    path('books/<int:id>/like'),
    path('books/<int:id>/unlike'),
    path('users/<int:id>'),
    path('logout')
]

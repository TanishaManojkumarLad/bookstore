
from django.urls import path
from .view import *
urlpatterns = [
    path('',  getRoutes),
    path('books/', getBooks),
    path('books/<str:pk>/', getBook),
]
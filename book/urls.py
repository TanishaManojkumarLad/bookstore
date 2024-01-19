from django.urls import path
from .views import *
urlpatterns = [
   path('', books, name="books"),
   path('book/<int:pk>/', book, name="book"),
   path('addbook/', addbook, name='addbook'),
   path('edit_book/<int:pk>/', editbook, name='edit_book'),
   path('delete_book/<int:pk>/', deletebook, name='delete_book'),
   path('register/', registerUser, name='register'),
   path('login/', user_login, name='login'),
   path('logout/', logout_view, name='logout')
]

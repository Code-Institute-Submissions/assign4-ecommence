from django.contrib import admin
from django.urls import path, include
import books.views


urlpatterns = [
    path('all', books.views.all_books, name="books"),
    path('create', books.views.create_book, name="create_book"),
    path('update/<book_id>', books.views.update_book, name="update_book"),
    path('delete/<book_id>', books.views.delete_book, name="delete_book"),
    path('authors/', books.views.all_authors, name="all_authors"),
    path('authors/create', books.views.create_author, name="create_author"),
    path('authors/update/<author_id>',
         books.views.update_author, name="update_author"),
    path('authors/delete/<author_id>',
         books.views.delete_author, name="delete_author"),

]

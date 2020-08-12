from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Book, Author
from .forms import BookForm, AuthorForm

# Create your views here.
# Home Page


def index(request):
    return render(request, 'books/index.template.html')


# create books page
def create_book(request):
    if request.method == "POST":
        # Submission data from User
        form = BookForm(request.POST)
        form.save()
        # show in all books view page
        return redirect(reverse(all_books))
    else:
        # create a new book form
        form = BookForm()
        return render(request, 'books/create_book.template.html', {
            'form': form
        })

# all books page


def all_books(request):
    all_books = Book.objects.all()
    return render(request, 'books/all_books.template.html', {
        'books': all_books
    })


# create authors page
def create_author(request):
    if request.method == "POST":
        # Submission data from User
        form = AuthorForm(request.POST)
        form.save()
        # show in all books view page
        return redirect(reverse(all_authors))
    else:
        # create a new book form
        form = AuthorForm()
        return render(request, 'books/create_author.template.html', {
            'form': form
        })

# all authors page


def all_authors(request):
    all_authors = Author.objects.all()
    return render(request, 'books/all_authors.template.html', {
        'authors': all_authors
    })

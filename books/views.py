from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Book, Author
from .forms import BookForm, AuthorForm, SearchForm

# Create your views here.
# Home Page


def index(request):
    return render(request, 'books/index.template.html')

# create books page


@ login_required
def create_book(request):
    if request.method == "POST":
        # Submission data from User
        form = BookForm(request.POST)
        # valid form
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            messages.success(request, "New Book has been added to the list!")
            # show in all books view page
            return redirect(reverse(all_books))
        else:
            return render(request, 'books/create_book.template.html', {
                'form': form
            })
    else:
        # create a new book form
        form = BookForm()
        return render(request, 'books/create_book.template.html', {
            'form': form
        })


# view book page
def view_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/view_books.template.html', {
        "book": book,
    })
# all books page


def all_books(request):
    form=SearchForm(request.GET)
    if request.GET:
        #create a query
        query = ~Q(pk__in=[]) #True Where 1
        
        #Get the title
        if 'title' in request.GET and request.GET['title']:
            print(request.GET)
            title_id= request.GET['title']
            print(title_id)
            query = query & Q(title__icontains=title_id)

        # select all the books
        all_books = Book.objects.all()

        #filter and reassign
        all_books =all_books.filter(query)
        number_of_books = all_books.count()
        return render(request, 'books/all_books.template.html', {
            'form':form,
            'books': all_books,
            'number_of_books': number_of_books,
        })
    else:
        # Search request not submitted
        all_books = Book.objects.all()
        number_of_books = all_books.count()
        return render(request, 'books/all_books.template.html', {
            'form':form,
            'books': all_books,
            'number_of_books': number_of_books,
        })

# update books page


@ login_required
def update_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    # Submitted form
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        form.save()
        return redirect(reverse(all_books))
    else:
        # extract the data from database
        form = BookForm(instance=book)
        return render(request, 'books/update_book.template.html', {
            'form': form
        })

# delete books page


@ login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    # submission
    if request.method == "POST":
        book.delete()
        return redirect(reverse(all_books))
    else:
        return render(request, 'books/delete_book.template.html', {
            'book': book})
# create authors page


@ login_required
def create_author(request):
    if request.method == "POST":
        # Submission data from User
        form = AuthorForm(request.POST)
        # valid form
        if form.is_valid():
            author = form.save(commit=False)
            author.owner = request.user
            author.save()
            messages.success(request, "New Author has been Added to the list!")
            # show in all books view page
            return redirect(reverse(all_authors))
        else:
            return render(request, 'books/create_author.template.html', {
                'form': form
            })
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
        'authors': all_authors,
    })
# view author page


def view_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'books/view_author.template.html', {
        "author": author
    })
# update authors page


@ login_required
def update_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    # submitted form
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        form.save()
        return redirect(reverse(all_authors))
    else:
        # extract data from database
        form = AuthorForm(instance=author)

        return render(request, 'books/update_author.template.html', {
                      'form': form,
                      'author': author
                      })
# delete author page


@ login_required
def delete_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    # submission
    if request.method == "POST":
        author.delete()
        return redirect(reverse(all_authors))
    else:
        return render(request, 'books/delete_author.template.html', {
            'author': author})

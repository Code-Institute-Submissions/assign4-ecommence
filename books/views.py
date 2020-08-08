from django.shortcuts import render

# Create your views here.
# Home Page


def index(request):
    return render(request, 'books/index.template.html')


#all book page
def all_books(request):
    return render(request,'books/all_books.template.html')
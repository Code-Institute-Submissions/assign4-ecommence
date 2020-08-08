from django.shortcuts import render

# Create your views here.
# Cart Page


def cart(request):
    return render(request, 'carts/cart.template.html')

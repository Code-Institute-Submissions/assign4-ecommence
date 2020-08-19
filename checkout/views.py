from django.shortcuts import render, get_object_or_404, HttpResponse, reverse, redirect
from django.contrib.sites.models import Site

# import in the settings
from django.conf import settings

# import in stripe
import stripe

# import in the book
from books.models import Book

# Create your views here.

def checkout(request):
    # tell Stripe what my api_key is
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # retrieve my shopping cart
    cart = request.session.get('shopping_cart', {})

    # create our line items
    line_items = []

    # stores all the ids of the books which we are purchasing
    all_book_ids = []

    # go through each book in the shopping cart
    for book_id, book in cart.items():
        # retrieve the book by its id from the database
        book_model = get_object_or_404(Book, pk=book_id)

        # create line item
        # you see all the possible properties of a line item at:
        # https://stripe.com/docs/api/invoices/line_item
        # amount in cents unit
        item = {
            "name": book_model.title,
            "amount": int(book_model.cost * 100),
            "quantity": book['qty'],
            "currency": "SGD",
         }

        line_items.append(item)
        all_book_ids.append(str(book_model.id))

    # get the current website
    current_site = Site.objects.get_current()

    # get the domain name
    domain = current_site.domain

    # create a payment session to represent the current transaction
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],  # take credit cards
        line_items=line_items,
        metadata={'all_books_id': ",".join(all_book_ids)},
        client_reference_id=request.user.id,
        success_url=domain + reverse("checkout_success"),
        cancel_url=domain + reverse("checkout_cancelled")
    )

    return render(request, "checkout/checkout.template.html", {
        "session_id": session.id,
        "public_key": settings.STRIPE_PUBLISHABLE_KEY
    })

    
def checkout_success(request):
    request.session["shopping_cart"] = {}
    messages.success(request, "Your purchases been completed")
    return redirect(reverse('books'))
    # return HttpResponse("checkout success")


def checkout_cancelled(request):
    return HttpResponse("checkout cancelled")
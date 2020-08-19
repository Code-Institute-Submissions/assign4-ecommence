from django.urls import path

import carts.views

urlpatterns = [

    path('add/<book_id>', carts.views.add_cart, name="add_cart"),
    path('view', carts.views.view_cart, name="view_cart"),
    path('remove/<book_id>', carts.views.remove_cart, name="remove_cart"),
    path('update_quantity/<book_id>', carts.views.update_quantity, name="update_cart_quantity")

]
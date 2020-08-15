from django.urls import path

import carts.views

urlpatterns = [

path('', carts.views.cart, name="carts")

]
from django.shortcuts import render

# Create your views here.

# About Us


def about_us(request):
    return render(request, "info/about_us.template.html")


# Contact Us


def contact_us(request):
    return render(request, "info/contact_us.template.html")

# terms and conditions


def terms_and_conditions(request):
    return render(request, "info/terms_and_conditions.template.html")

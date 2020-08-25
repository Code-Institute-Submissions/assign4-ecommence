from django.urls import path
import info.views

urlpatterns = [
    path('about_us/', info.views.about_us, name="about_us"),
    path('contact_us/', info.views.contact_us, name="contact_us"),
    path('terms_and_conditions/', info.views.terms_and_conditions, name="terms_and_conditions"),
]
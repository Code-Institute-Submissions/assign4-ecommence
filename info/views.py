from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

# About Us


def about_us(request):
    return render(request, "info/about_us.template.html")


# Contact Us


def contact_us(request):
    form = ContactForm
    
    if request.method == 'POST':
        form = form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the contact information
            template = get_template('info/contact_us.template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            messages.success(request, "Thank you for your query. We will contact you shortly.")
            return redirect('home')
            
    return render(request, "info/contact_us.template.html", {
        'form':form
    })
    

# terms and conditions


def terms_and_conditions(request):
    return render(request, "info/terms_and_conditions.template.html")

from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.shortcuts import redirect, render
from .forms import ContactForm
from django.http import HttpResponse

# Create your views here.

def index(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.changed_data['email']
            message = form.cleaned_data['message']
            name = form.changed_data['name']
            try:
                send_mail(message, name , email, settings.EMAIL_HOST_USER, ['masih.javidan69@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Not found')
            return redirect('success')

        else:
            form = ContactForm
    
    context = {
        'form': form,
    }
    
    return render(request, 'contact/contact.html', context)

def successViews(request):
    return HttpResponse('Success your message, Thamk you')
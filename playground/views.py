from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, send_mass_mail, BadHeaderError, EmailMessage


# Create your views here.

def welcome(request):
    return render(request, 'hello.html', context={})


def hello_user(request, name):
    try:
        message = f'hello {name}, you have been posting rubbish on our platform, we will ban you'
        mail = EmailMessage('warning', message, 'complaints@twitter.com', ['seyi69@email.com'])
        mail.attach_file('playground/static/images/images.jpeg')
        mail.send()
    except BadHeaderError:
        pass
    return render(request, template_name='user.html', context={'name': name})


def print_one(request, num):
    return render(request, template_name='print.html', context={'num': num})

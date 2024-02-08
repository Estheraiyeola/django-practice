from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def welcome(request):
    return render(request, 'hello.html', context={})


def hello_user(request, name):
    return render(request, template_name='user.html', context={'name': name})


def print_one(request, num):
    return render(request, template_name='print.html', context={'num': num})

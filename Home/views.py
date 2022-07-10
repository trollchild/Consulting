
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings


def Page(request):
    context = {}
    return render(request, 'Test.html', context)

def Projects(request):
    Project = "project"
    context = {'Projects':Projects}
    return render(request, 'Projects.html', context)

def Finnish(request):
    Finnish = "Finnish"
    context = {'Finnish':Finnish}
    return render(request, 'Test.html', context)

def Projektit(request):
    Finnish = "Finnish"
    context = {'Finnish':Finnish}
    return render(request, 'Projects.html', context)


# Create your views here.

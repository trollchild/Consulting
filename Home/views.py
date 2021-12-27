from django.shortcuts import render, redirect, reverse
import logging #this will be deleted when we fix all debugs (on debug = false)
from django.http import HttpResponse, Http404, JsonResponse

def Page(request):
    context = {}
    return render(request, '/Test.HTML', context)


# Create your views here.

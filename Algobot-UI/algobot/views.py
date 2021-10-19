from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader


def index(request):
    return render(request, 'algobot/index.html')


def login(request):
    return render(request, 'algobot/login.html')

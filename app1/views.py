from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def str_app1(request):
    return HttpResponse('<center><h1>String Response from app1</h1></center>')
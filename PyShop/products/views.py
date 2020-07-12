from django.http import HttpResponse
from django.shortcuts import render

# /products > index
def index(request):
    return HttpResponse("Hello World!")

    

import re
from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("This is my response!")

# Create your views here.

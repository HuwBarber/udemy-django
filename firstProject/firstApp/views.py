from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def display(request):
    return HttpResponse("<h1>My First Django App!</h1>")

def displayDatetime(request):
    return HttpResponse(f"Current datetime: {datetime.datetime.now()}")

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h6> hello boys</h6>")

def info(request):
    return HttpResponse("<h2> Bye bye </h2>")
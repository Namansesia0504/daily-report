from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return render  (request,"index.html")

def success_page(request):
    return HttpResponse("<h1>Hey this is a success page</h1> ")

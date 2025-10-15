from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>HellO</h1>")

def new(request):
    return HttpResponse("<h1>Page === New</h1>")

def data(request):
    return HttpResponse("<h1>Page === Data</h1><a href=\"test\">На тест</a>")

def test(request):
    return HttpResponse("<h1>Page === Test</h1><a href=\"data\">На дата</a>") 
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("<h1>HellO</h1>")
    return render(request,'main/index.html')

def new(request):
    #return HttpResponse("<h1>Page === New</h1>")
    return render(request,'main/new.html')

def new2(request):
    #return HttpResponse("<h1>Page === New</h1>")
    return render(request,'main/new2.html')

def new3(request):
    #return HttpResponse("<h1>Page === New</h1>")
    return render(request,'main/new3.html')

def data(request):
    return HttpResponse("<h1>Page === Data</h1><a href=\"test\">На тест</a>")


def test(request):
    return HttpResponse("<h1>Page === Test</h1><a href=\"data\">На дата</a>") 

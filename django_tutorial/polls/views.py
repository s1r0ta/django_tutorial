from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, "index.html") 
def zov(request):
    return HttpResponse("<h1>РОССИЯ ПУТИН ПОБЕДА<h1>")
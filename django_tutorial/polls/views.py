from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>я тибя убью<h1>")
def vilka(request):
    return HttpResponse("<h1>вiлка<h1>")
def lozhka(request):
    return HttpResponse("<h1>лололошка<h1>")
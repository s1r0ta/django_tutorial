from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>Привет! С вами говорит Hitler_1488!<h1>")
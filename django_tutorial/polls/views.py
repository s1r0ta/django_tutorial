from django.contrib import messages
from django.db.models import F,Sum
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})
def index(request):
    latest_question_list = Question.objects.annotate(total_votes=Sum("choice__votes")).order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, 'index.html', context)
def zov(request):
    return HttpResponse("<h1>РОССИЯ ПУТИН ПОБЕДА<h1>")
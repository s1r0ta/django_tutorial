from django.contrib import messages
from django.db.models import F,Sum
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Choice

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})

def index(request):
<<<<<<< HEAD
    return HttpResponse("<h1>я тибя убью<h1>")
def vilka(request):
    return HttpResponse("<h1>вiлка<h1>")
def lozhka(request):
    return HttpResponse("<h1>лололошка<h1>")
=======
    latest_question_list = Question.objects.annotate(total_votes=Sum("choice__votes")).order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, 'index.html', context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render (request, "detail.html",{
            "question" : question,
            "error_message": "сначала выберите вариант ответа",
        })
    selected_choice.votes = F("votes") + 1
    selected_choice.save()
    messages.success(request, "спасибо! ваш голос учтен")
    return HttpResponseRedirect(reverse("results", args=(question.id,)))

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = list(question.choice_set.all())
    total = sum(choice.votes for choice in choices)
    for choice in choices:
        choice.percent = round(choice.votes * 100 / total) if total else 0
    context = {"question": question , "choices":choices ,"total":total}
    return render(request, "results.html", context)    
>>>>>>> 55b8074

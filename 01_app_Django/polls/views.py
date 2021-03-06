from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from polls.models import Questions, choice

# Create your views here.
def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'polls/index.html', context)   
    
def detail(request, question_id):
    '''This will run when calling the detail function,'''
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, "polls/detail.html", {'question': question})

def results(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'polls/result.html', {'question': question, })

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")

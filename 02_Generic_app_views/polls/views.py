from re import template
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views import View
from polls.models import Questions, choice

# Create your views here.
'''Function Based Views'''
# def IndexView(request):
#     latest_question_list = Questions.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list' : latest_question_list}
#     return render(request, 'polls/index.html', context)   
    
# def detail(request, question_id):
#     '''This will run when calling the detail function,'''
#     question = get_object_or_404(Questions, pk=question_id)
#     return render(request, "polls/detail.html", {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Questions, pk=question_id)
#     return render(request, 'polls/result.html', {'question': question, })

# def vote(request, question_id):
#     return HttpResponse(f"You're voting on question {question_id}.")

'''Class Based view'''

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Questions.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Questions
    template_name = 'polls/detail.html'
    context_object_name = 'question'

class ResultView(generic.DetailView):
    model = Questions
    template_name = 'polls/result.html'
    context_object_name = 'question'

def vote(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing with POST data. This prevents data from being posted twice if a user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

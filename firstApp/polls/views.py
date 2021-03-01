from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Question

def index(request):
    latestQuestionList = Question.objects.order_by('-pubDate')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latestQuestionList': latestQuestionList,
    }
    return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))
    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    
    return render(request, 'polls/details.html', {'question' : question})
    # return HttpResponse("You're looking at question %s" % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message' : "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
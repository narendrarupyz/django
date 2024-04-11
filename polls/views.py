#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from  django.template import loader
from django.shortcuts import get_object_or_404,render
from django.views import generic

'''def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {'latest_question_list':latest_question_list,}
   
   # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html',context)'''
#After Amend views
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest question list'

    def get_queryset(self):
        """"Returned the last five published questions."""
        return Question.objects.order_by('-public_date')[:5]

'''def index(request):
    return HttpResponse("hello world you are at the poll index.")'''

'''def detail(request, question_id):
    try:
        question = Question.objects.get(pk= question_id)
    except Question.DoesNotExist:
        raise Http404("Question doesn't exist")
    return render(request, 'polls/detail.html',{'question' : question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html',{'question' : question})'''
#After Amend views
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


'''def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})'''
#After Amend views
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_messgage' : "You didn't select choice.",
        
        })
    else:
        select_choice.votes +=1
        select_choice.save()
         # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



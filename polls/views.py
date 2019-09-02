from django.http import HttpResponse
from django.template import loader
from .models import Question
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list,
    }
    return HttpResponse(template.render(context,request))

def results(request,question_id):
    response = "You are looking for the result of the question %s."
    return HttpResponse(response % question_id)

def detail(request,question_id):
    response = ("Question %s." % question_id)
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Voting on question %s." % question_id)

def add(request,question_id):
    return HttpResponse("Delete on question %s." % question_id)


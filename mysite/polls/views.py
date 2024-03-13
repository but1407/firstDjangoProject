from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
import numpy as np
# Create your views here.


def index(request):
    myname ='but'
    taisan =['phone', 'plane','bike','car']
    return render(request,"polls/index.html",{'myname':myname, 'taisan':taisan})
def products(request):
    return HttpResponse("<h1>San pham</h1>")
def viewlists(request):
    list_question = Question.objects.all()
    # list_question = get_object_or_404(Question, pk=1)
    is_array = isinstance(list_question, object)
    list_question = list_question if is_array else {list_question}
    return render(request,"polls/question_list.html",{'list_question': list_question})

def detailView(request, question_id):
    q =  Question.objects.get(pk=question_id)
    return render(request, "polls/detail_question.html",{'qs': q})

def vote(request, question_id):
    q= Question.objects.get(pk=question_id)
    dulieu = request.POST["choice"]
    c = q.choice_set.get(pk = dulieu)
    c.vote = c.vote + 1 
    c.save()
    return render(request,"polls/result.html",{"qs":q})
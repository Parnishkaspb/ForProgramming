from django.shortcuts import render
from django.views.generic import ListView, DetailView

from django.http import HttpResponse

from .models import Question, Answer

first = True

def index(request):
    # print(returnFirstID(1)[0]['id'])
    context = {
        'new': returnFirstID(1)[0]['id'],
        'profi': returnFirstID(2)[0]['id'],
        'expert': returnFirstID(3)[0]['id'],
    }

    return render(request, 'practice/start.html', context=context)

def new(request, id):
    return render(request, 'practice/new.html', {'question': createtask(1,id)['question'], 'answers':  createtask(1,id)['answers'], 'next': createtask(1,id)['next']})

def profi(request, id):
    return render(request, 'practice/new.html', {'question': createtask(2,id)['question'], 'answers':  createtask(2,id)['answers'], 'next': createtask(2,id)['next']})

def expert(request, id):
    return render(request, 'practice/new.html', {'question': createtask(3,id)['question'], 'answers':  createtask(3,id)['answers'], 'next': createtask(3,id)['next']})


def final(request):
    return render(request, 'practice/final.html')


def createtask(whatTypeQuestion, id):
    allquestion = Question.objects.filter(type=whatTypeQuestion).values('id')
    s = []
    for i in allquestion:
        s.append(str(i['id']))
    
    try:
        next = int(s.index(f'{id}'))+1
        next = s[next] 
    except:
        next = -1
    
    question = Question.objects.get(pk=id)
    answers = Answer.objects.filter(question=id)

    return {'question': question, 'answers': answers, 'next': next}


def returnFirstID(whatTypeQuestion):
    return Question.objects.filter(type=whatTypeQuestion).values('id')[:1]
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice

# Create your views here.

# def index(request):
#     response = HttpResponse()
#     response.write("<h1>Welcome</h1>")
#     response.write("This is the polls app")
#     return response

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    print(question_id)
    return HttpResponse("You're looking at question %s." %question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You'ra voting on question %s." %question_id)
from .models import Person
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    listname = Person.objects.order_by('-name')
    ouput = '\n '.join(q.name for q in listname)
    return HttpResponse(ouput)

def detail(request, id):
    list = Person.objects()
    output = '\n'.join()
    return HttpResponse(output)
    
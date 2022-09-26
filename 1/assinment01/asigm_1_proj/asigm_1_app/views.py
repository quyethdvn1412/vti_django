from .models import Person
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
# Create your views here.

def index(request):
    list_people = Person.objects.order_by('-name')
    template = loader.get_template('asigm_1_app/index.html')
    content = {
        'list_people' : list_people
    }
    return HttpResponse(template.render(content, request))

def detail(request, id):
    try:
        info = Person.objects.get(pk=id)
    except Person.DoesNotExist:
        raise Http404('The people of %s does not exist.', id)
    return render(request, 'asigm_1_app/detail.html', {'id' :id})
    
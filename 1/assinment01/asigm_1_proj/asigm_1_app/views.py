from .models import Person
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

# Create your views here.

def index(request):
    list_people = Person.objects.order_by('id')
    template = loader.get_template('asigm_1_app/index.html')
    content = {
        'list_people' : list_people,
    }
    return HttpResponse(template.render(content, request))

def detail(request, id):
    info = Person.objects.get(pk=id)
    template = loader.get_template('asigm_1_app/detail.html')
    content = {
        'person': info,
    }
    return HttpResponse(template.render(content, request))

def add(request):
    template = loader.get_template('asigm_1_app/add.html')
    content = {}
    return HttpResponse(template.render(content, request))

def add_new_user(request):
    new_user = Person(name = request.POST['name'], age = request.POST['age'], address = request.POST['address'], mobile_number = request.POST['mobile_number'])
    new_user.save()
    response = HttpResponse()
    response.write("<h1>User </h1>" + request.POST['name'] + "of information added." + "</br>")
    return HttpResponseRedirect(reverse('asigm_1_app:index.html'))
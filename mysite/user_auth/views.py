from django.shortcuts import render
from .forms import RegisterForm
from django.http import HttpResponse
# Create your views here.

def register(request):
    if request.method == "POST":
        response = HttpResponse()
        response.write("<h1>!!! Thanks for registering !!!</h1></br>")
        response.write("Your Username: " + request.POST['username'] + "</br>")
        response.write("Your Mail: " + request.POST['mail'] + "</br>")
        return response
    
    registerForm = RegisterForm()
    return render(request, 'user-auth/register.html', {'form': registerForm})
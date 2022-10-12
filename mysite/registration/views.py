from email import message
from django import forms
from django.shortcuts import render
from . import forms

# Create your views here.

def regform(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        if form.is_valid():
            message = 'Thank U!'
        else:
            message = 'Data is invalid, try again!'
    else:
        message = 'Input your information to register!'
    return render(request, 'signup.html', {'message': message, 'form': form})
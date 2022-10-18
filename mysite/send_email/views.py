from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import EmailForm

# Create your views here.

def sendMail(request):
    messageSent = False
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
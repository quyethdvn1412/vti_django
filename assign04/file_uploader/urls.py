from django.urls import path
from . import views

app_name = 'assign04'

urlpatterns =[
    path('', views.fileUploaderView),
]
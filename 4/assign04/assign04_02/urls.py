from django.urls import path
from . import views

app_name = 'assign04_02'

urlpatterns = [
    path('', views.index, name='index'),
]
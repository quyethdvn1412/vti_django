from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Display all people
    path('<int:id>', views.detail, name='detail'),
]
from django.urls import path
from . import views

app_name = 'asigm_1_app'
urlpatterns = [
    path('', views.index, name='index'),
    # Display all people
    path('<int:id>', views.detail, name='detail'),
]
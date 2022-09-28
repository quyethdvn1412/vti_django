from django.urls import path
from . import views

app_name = 'asigm_1_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
    path('add-new-user/', views.add_new_user, name='AddNewUser'),
]
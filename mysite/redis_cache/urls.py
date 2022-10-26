from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.get_products, name='index'),
    path('cache/', views.get_products_with_cached, name='cached'),
]

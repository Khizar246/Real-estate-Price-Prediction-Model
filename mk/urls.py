from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('result', views.result, name='Result'),
    # path('result', views.output, name='output'),
    ]

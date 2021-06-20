from django.urls import path, include
from . import views

appname = 'weather'
urlpatterns = [
    path('', views.index),

]
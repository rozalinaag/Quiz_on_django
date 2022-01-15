from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # go to views.py in function index
    path('results', views.results, name='results'),
    path('question1', views.question1, name='question1'),
    path('question2', views.question2, name='question2'),
    path('question3', views.question3, name='question3'),
    path('question4', views.question4, name='question4'),
    path('question5', views.question5, name='question5'),
]
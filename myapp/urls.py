from django.urls import path
from . import views

#list is gonna take all the urls in the project
urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter')
]
#if its empty inside '' it means its the home page/root page
#views.intex is the function/action that will be called when the user goes to the home page
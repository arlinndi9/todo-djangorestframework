from django.urls import path
from webapi.views import *
urlpatterns = [

    #path('todoapi',Todoapi.as_view(),name='todos'),
    path('',TodoListCreate.as_view(),name='todos'),
    path('todoapi/<int:pk>/',DetailTodo.as_view(),name='todos'),

]

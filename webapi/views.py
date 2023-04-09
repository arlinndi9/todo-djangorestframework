from django.shortcuts import render
from .models import Todos
from webapi.serializers import TodosSerializer
from rest_framework import generics
# Create your views here.



class Todoapi(generics.ListAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer

class TodoListCreate(generics.ListCreateAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer
from rest_framework import generics
from .models import Task
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import TaskSerializer
from rest_framework.views import APIView


class TaskListCreateView(generics.ListCreateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer



# class TasksAPIView(APIView):
#     def get(self, request):

#         t=Task.objects.all()
#         return Response({'post':TaskSerializer(t, many=True).data})
    
#     def post(self, request):




# class TasksAPIView(generics.ListAPIView):
#     queryset=Task.objects.all()
#     serializer_class=TaskSerializer

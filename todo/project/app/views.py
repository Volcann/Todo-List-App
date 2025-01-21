from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .serializers import TODOSerializer

from .models import TODO

def todo_list(request):  # Renamed the function to avoid conflict
    data = {
        "message": "Hello, Django!",
        "status": "success"
    }
    return JsonResponse(data)

@api_view(['GET'])
def apioverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',  # Missing comma added here
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pR>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def todolist(request):
    tasks = TODO.objects.all()  # Accessing the 'TODO' model
    serializer = TODOSerializer(tasks, many=True)
    return Response(serializer.data)
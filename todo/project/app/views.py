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

@api_view(['GET'])
def taskdetail(request, pk):
    tasks = TODO.objects.get(id=pk)  # Accessing the 'TODO' model
    serializer = TODOSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskcreate(request):
    serializer = TODOSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)  # Status 201 for created
    return Response(serializer.errors, status=400)  # Status 400 for bad request

@api_view(['POST'])
def taskupdate(request, pk):
    tasks = TODO.objects.get(id=pk)
    serializer = TODOSerializer(instance=tasks, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)  # Status 201 for created
    return Response(serializer.errors, status=400)  # Status 400 for bad request

@api_view(['DELETE'])
def taskdelete(request, pk):
    try:
        # Fetch the task to be deleted
        task = TODO.objects.get(id=pk)
    except TODO.DoesNotExist:
        return Response({"error": "Task not found"}, status=404)

    # Delete the task
    task.delete()
    return Response({"message": "Task deleted successfully!"}, status=204) 
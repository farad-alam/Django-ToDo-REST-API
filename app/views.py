from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from .models import Task
# Create your views here.

@api_view(['GET'])
def task_list(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH', 'GET'])
def update_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'error':'task not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        serializer = TaskSerializer(task, data=request.data)
    else:
        serializer = TaskSerializer(task, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', 'GET'])
def delete_task(request,pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'error':'task not found'}, status=status.HTTP_404_NOT_FOUND)
    task.delete()
    return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
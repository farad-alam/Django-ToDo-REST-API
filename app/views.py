from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from .models import Task
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import TaskFilter
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.decorators import throttle_classes

class TaskListPagination(PageNumberPagination):
    page_size = 5  # Number of tasks per page
    page_size_query_param = 'page_size'  # Allow clients to change the page size with a query parameter
    max_page_size = 100  # Max limit for page size



#   API VIEW
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def task_list(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)

    return Response(serializer.data)

class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = TaskListPagination  # Apply custom pagination class
    throttle_classes = [UserRateThrottle]  # Apply throttling to class-based view

    
    # Define the fields that can be filtered, searched, and sorted
    filterset_class = TaskFilter  # Use the custom filterset for filtering
    search_fields = ['title', 'description']  # Allow searching by title and description
    ordering_fields = ['title', 'priority','created_date', 'due_date', 'status']  # Allow sorting by created date, due date, and status
    ordering = ['created_date']  # Default ordering

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH', 'GET'])
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
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

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def delete_task(request,pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return JsonResponse({'error':'task not found'}, status=status.HTTP_404_NOT_FOUND)
    task.delete()
    return JsonResponse({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)













# TEMPLATE RENDER VIEW ----------->>>>>

def home(request):

    return render( request,'home.html')

def task_list_view(request):

    return render( request,'task_list.html')


def create_task_view(request):

    return render(request, 'create_task.html')

def update_task_view(request, pk):
    
    return render(request, 'edit_task.html', {'task_id': pk})
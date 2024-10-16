from django.urls import path
from .views import (
    task_list, 
    create_task, 
    update_task, 
    delete_task, 
    task_list_view,
    create_task_view,
    update_task_view,
    TaskListView
    )

urlpatterns = [
    # api url
    path('task-list/', TaskListView.as_view(), name='task_list'),
    path('create-task/', create_task, name='create-task'),
    path('update-task/<int:pk>/', update_task, name='update-task'),
    path('delete/<int:pk>/', delete_task, name='delete-task'),


    # template url
    path('task-list-view/', task_list_view, name='task-list-view'),
    path('create-task-view/', create_task_view, name='create-task-view'),
    path('update-task-view/<int:pk>/', update_task_view, name='update-task-view'),
]

from django.urls import path
from .views import task_list, create_task, update_task, delete_task

urlpatterns = [
    path('task-list/', task_list, name='task_list'),
    path('create-task/', create_task, name='create-task'),
    path('update-task/<int:pk>/', update_task, name='update-task'),
    path('delete/<int:pk>/', delete_task, name='delete-task')
]

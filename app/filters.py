import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = {
            'status': ['exact'],  # Filter by exact match of status (e.g., "completed", "pending")
            'due_date': ['gte', 'lte'],  # Filter by range of dates
            'created_date': ['gte', 'lte'],  # Filter by creation date range
        }

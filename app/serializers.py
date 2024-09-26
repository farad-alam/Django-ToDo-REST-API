from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    # created_date = serializers.CharField(read_only=True,)
    # updated_date = serializers.CharField(read_only=True, )

    class Meta:
        model = Task
        fields = ['id','title', 'description', 'created_date', 'due_date', 'priority', 'status', 'category', 'assigned_user', 'updated_date']
        read_only_fields = ['created_date', 'updated_date']
from django.db import models
from django.conf import settings
from django.db.models.functions import Lower
from django.db.models import Case, When, IntegerField

class TaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(
            priority_order=Case(
                When(priority='H', then=1),
                When(priority='M', then=2),
                When(priority='L', then=3),
                output_field=IntegerField(),
            )
        )

    def order_by_title(self, order):
        return self.get_queryset().order_by(Lower('title') if order == 'asc' else Lower('title').desc())


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]
    
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('I', 'In Progress'),
        ('C', 'Completed'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    # completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    category = models.CharField(max_length=50, blank=True, null=True)
    assigned_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')    
    updated_date = models.DateTimeField(auto_now=True)


    objects = TaskManager()

    def __str__(self):
        return self.title


from django.db import models

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=300)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)

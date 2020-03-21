from django.db import models

class Todo(models.Model):
    content = models.CharField(max_length=200)
    due_date = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    
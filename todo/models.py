from django.db import models


class TaskDetails(models.Model):
    task = models.CharField(max_length=300)
    priority = models.IntegerField()
    date = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task
